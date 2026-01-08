from __future__ import annotations

import argparse
import logging
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .evaluate import evaluate_regression
from .preprocess import clean_data, feature_engineering, load_raw, save_processed

# Logging yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def ensure_dirs(project_root: Path) -> dict[str, Path]:
    processed_dir = project_root / "data" / "processed"
    reports_dir = project_root / "reports"
    figures_dir = reports_dir / "figures"

    processed_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    return {
        "processed_dir": processed_dir,
        "reports_dir": reports_dir,
        "figures_dir": figures_dir,
    }


def _drop_datetime_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    date_cols = [col for col in df.columns if "date" in col.lower()]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    dt_cols = df.select_dtypes(include=["datetime64[ns]", "datetime64[ns, UTC]"]).columns
    if len(dt_cols) > 0:
        df = df.drop(columns=dt_cols)
    return df


def _normalize_column_name(name: str) -> str:
    return "".join(ch.lower() for ch in name if ch.isalnum())


def _drop_geo_columns(df: pd.DataFrame, drop_geo: bool) -> pd.DataFrame:
    if not drop_geo:
        return df
    targets = {"city", "postalcode", "state"}
    drop_cols = [col for col in df.columns if _normalize_column_name(col) in targets]
    return df.drop(columns=drop_cols, errors="ignore")


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    num_cols = X.select_dtypes(include="number").columns.tolist()
    cat_cols = [col for col in X.columns if col not in num_cols]

    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, num_cols),
            ("cat", categorical_transformer, cat_cols),
        ]
    )


def get_feature_names(preprocessor: ColumnTransformer) -> list[str]:
    try:
        return preprocessor.get_feature_names_out().tolist()
    except AttributeError:
        names: list[str] = []
        for name, transformer, cols in preprocessor.transformers_:
            if name == "remainder":
                continue
            if isinstance(transformer, Pipeline):
                transformer = transformer.steps[-1][1]
            if hasattr(transformer, "get_feature_names_out"):
                try:
                    part = transformer.get_feature_names_out(cols)
                except TypeError:
                    part = transformer.get_feature_names_out()
                names.extend([str(item) for item in part])
            elif hasattr(transformer, "get_feature_names"):
                try:
                    part = transformer.get_feature_names(cols)
                except TypeError:
                    part = transformer.get_feature_names()
                names.extend([str(item) for item in part])
            else:
                if isinstance(cols, (list, tuple, pd.Index)):
                    names.extend([str(col) for col in cols])
                else:
                    names.append(str(cols))
        return names


def compute_log_shift(y: pd.Series) -> float:
    values = pd.to_numeric(y, errors="coerce")
    min_val = values.min()
    if pd.isna(min_val):
        return 0.0
    if min_val <= -0.999:
        return float(-min_val + 1.0)
    return 0.0


def make_log_transform(shift: float):
    def _transform(values):
        return np.log1p(values + shift)

    def _inverse(values):
        return np.expm1(values) - shift

    return _transform, _inverse


def build_summary(df: pd.DataFrame) -> str:
    rows, cols = df.shape
    num_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = [col for col in df.columns if col not in num_cols]
    missing_total = int(df.isna().sum().sum())
    missing_by_col = df.isna().sum()
    nonzero_missing = missing_by_col[missing_by_col > 0]

    lines = [
        f"Satir sayisi: {rows}",
        f"Kolon sayisi: {cols}",
        f"Sayisal kolonlar ({len(num_cols)}): {', '.join(num_cols) if num_cols else 'Yok'}",
        f"Kategorik kolonlar ({len(cat_cols)}): {', '.join(cat_cols) if cat_cols else 'Yok'}",
        f"Toplam eksik deger: {missing_total}",
    ]

    if nonzero_missing.empty:
        lines.append("Kolona gore eksik: Yok")
    else:
        lines.append("Kolona gore eksikler:")
        for col, count in nonzero_missing.items():
            lines.append(f"- {col}: {int(count)}")

    return "\n".join(lines)


def train_models(
    df: pd.DataFrame, target: str, drop_geo: bool = False
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if target not in df.columns:
        raise ValueError("Profit kolonu bulunamadi")

    X = df.drop(columns=[target])
    if target.lower() == "profit":
        drop_cols = [col for col in X.columns if col.lower() == "profit_margin"]
        if drop_cols:
            X = X.drop(columns=drop_cols)
    X = _drop_geo_columns(X, drop_geo)
    y = df[target]
    X = _drop_datetime_columns(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    preprocessor = build_preprocessor(X_train)
    shift = compute_log_shift(y_train)
    transform, inverse = make_log_transform(shift)
    models = {
        "LinearRegression": TransformedTargetRegressor(
            regressor=LinearRegression(), func=transform, inverse_func=inverse
        ),
        "RandomForestRegressor": TransformedTargetRegressor(
            regressor=RandomForestRegressor(
                n_estimators=200,
                min_samples_leaf=2,
                max_features="sqrt",
                random_state=42,
                n_jobs=-1,
            ),
            func=transform,
            inverse_func=inverse,
        ),
    }

    metrics_rows = []
    top10_df = pd.DataFrame(columns=["feature", "importance"])

    for name, model in models.items():
        pipeline = Pipeline(
            steps=[
                ("preprocess", clone(preprocessor)),
                ("model", model),
            ]
        )
        pipeline.fit(X_train, y_train)
        preds = pipeline.predict(X_test)
        metrics = evaluate_regression(y_test, preds)
        metrics_rows.append({"model": name, **metrics})

        if name == "RandomForestRegressor":
            model_step = pipeline.named_steps["model"]
            regressor = getattr(model_step, "regressor_", None) or getattr(
                model_step, "regressor", None
            )
            if regressor is not None and hasattr(regressor, "feature_importances_"):
                importances = regressor.feature_importances_
                feature_names = get_feature_names(pipeline.named_steps["preprocess"])
                if len(feature_names) != len(importances):
                    feature_names = [f"feature_{idx}" for idx in range(len(importances))]
                order = importances.argsort()[::-1][:10]
                top10_df = pd.DataFrame(
                    {
                        "feature": [feature_names[idx] for idx in order],
                        "importance": [float(importances[idx]) for idx in order],
                    }
                )

    metrics_df = pd.DataFrame(metrics_rows)
    return metrics_df, top10_df


def main() -> None:
    """Ana is akisi fonksiyonu - CLI ile calistirilabilir."""
    parser = argparse.ArgumentParser(
        description="VB_DS Kar Tahmini Is Akisi - Veri temizleme, ozellik muhendisligi ve model egitimi"
    )
    parser.add_argument(
        "--drop-geo",
        action="store_true",
        help="City/State/Postal Code kolonlarini cikar (Geo yok ablasyon testi)"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Rastgelelik tohumu (tekrarlanabilirlik icin, varsayilan: 42)"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="reports",
        help="Cikti dizini (varsayilan: reports/)"
    )
    
    args = parser.parse_args()
    
    project_root = Path(__file__).resolve().parents[1]
    
    # Output dizini oluştur
    output_dir = project_root / args.output_dir
    dirs = ensure_dirs(project_root)
    
    logging.info(f"Is akisi baslatildi - Tohum: {args.seed}, Geo cikarma: {args.drop_geo}")
    logging.info(f"Proje kök dizini: {project_root}")
    logging.info(f"Çıktı dizini: {output_dir}")

    raw_path = project_root / "data" / "raw" / "SampleSuperstore.csv"
    if not raw_path.exists():
        logging.error(f"Ham veri bulunamadı: {raw_path}")
        logging.error("Lütfen SampleSuperstore.csv dosyasını data/raw/ klasörüne koyun.")
        raise FileNotFoundError(
            f"SampleSuperstore.csv bulunamadi. Beklenen konum: {raw_path}"
        )
    
    logging.info(f"Ham veri yükleniyor: {raw_path}")
    df = load_raw(raw_path)
    logging.info(f"Ham veri yüklendi: {len(df)} satır, {len(df.columns)} kolon")
    
    logging.info("Veri temizleniyor...")
    df = clean_data(df)
    
    logging.info("Ozellik muhendisligi yapiliyor...")
    df = feature_engineering(df)

    processed_path = dirs["processed_dir"] / "clean.csv"
    logging.info(f"Temizlenmiş veri kaydediliyor: {processed_path}")
    save_processed(df, processed_path)

    summary_text = build_summary(df)
    summary_path = dirs["reports_dir"] / "data_summary.txt"
    summary_path.write_text(summary_text, encoding="utf-8")
    logging.info(f"Veri özeti kaydedildi: {summary_path}")

    logging.info("Model egitimi basliyor (Tam - tum kolonlarla)...")
    metrics_full, top10_df = train_models(df, target="Profit", drop_geo=False)
    
    logging.info("Model egitimi basliyor (Geo Yok - City/State/Postal Code haric)...")
    metrics_no_geo, _ = train_models(df, target="Profit", drop_geo=True)

    logging.info("Metrikler kaydediliyor...")
    metrics_full.to_csv(dirs["reports_dir"] / "metrics.csv", index=False)
    metrics_full.to_csv(dirs["reports_dir"] / "metrics_full.csv", index=False)
    metrics_no_geo.to_csv(dirs["reports_dir"] / "metrics_no_geo.csv", index=False)
    top10_df.to_csv(dirs["reports_dir"] / "top10_importance.csv", index=False)

    logging.info("✓ Is akisi tamamlandi!")
    logging.info(f"Çıktılar: {dirs['reports_dir']}/")
    print("Tamam: ciktilar uretildi")


if __name__ == "__main__":
    main()
