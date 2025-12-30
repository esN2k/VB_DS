from __future__ import annotations

import argparse
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

from evaluate import evaluate_regression


def load_processed(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


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


def prepare_features(df: pd.DataFrame, target: str, drop_geo: bool = False):
    if target not in df.columns:
        raise ValueError(f"Target column not found: {target}")

    y = df[target]
    X = df.drop(columns=[target])
    if target.lower() == "profit":
        drop_cols = [col for col in X.columns if col.lower() == "profit_margin"]
        if drop_cols:
            X = X.drop(columns=drop_cols)
    X = _drop_geo_columns(X, drop_geo)
    X = _drop_datetime_columns(X)
    return X, y


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


def train_and_evaluate(X_train, X_test, y_train, y_test):
    base_preprocessor = build_preprocessor(X_train)
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

    for name, model in models.items():
        pipeline = Pipeline(
            steps=[
                ("preprocess", clone(base_preprocessor)),
                ("model", model),
            ]
        )
        pipeline.fit(X_train, y_train)
        preds = pipeline.predict(X_test)
        metrics = evaluate_regression(y_test, preds)
        print(
            f"{name} - MAE: {metrics['mae']:.4f}, "
            f"RMSE: {metrics['rmse']:.4f}, R2: {metrics['r2']:.4f}"
        )
        if name == "RandomForestRegressor":
            model_step = pipeline.named_steps["model"]
            regressor = getattr(model_step, "regressor_", None) or getattr(
                model_step, "regressor", None
            )
            if regressor is not None and hasattr(regressor, "feature_importances_"):
                importances = regressor.feature_importances_
                feature_names = get_feature_names(pipeline.named_steps["preprocess"])
                if len(feature_names) == len(importances):
                    order = importances.argsort()[::-1][:10]
                    print("RandomForest feature importances (top 10):")
                    for idx in order:
                        print(f"  {feature_names[idx]}: {importances[idx]:.4f}")
                else:
                    print("RandomForest feature importances unavailable: name mismatch")
            else:
                print("RandomForest feature importances unavailable: model mismatch")


def main() -> None:
    parser = argparse.ArgumentParser(description="Train regression models")
    parser.add_argument("--input", required=True, help="Path to processed CSV")
    parser.add_argument("--target", default="Profit", help="Target column name")
    parser.add_argument("--test-size", type=float, default=0.2, help="Test split ratio")
    parser.add_argument(
        "--drop-geo",
        action="store_true",
        help="Drop City/Postal Code/State for generalization test",
    )
    args = parser.parse_args()

    df = load_processed(args.input)
    X, y = prepare_features(df, args.target, drop_geo=args.drop_geo)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=42
    )

    train_and_evaluate(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    main()
