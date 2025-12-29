from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, Optional

import pandas as pd


def load_raw(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)


def _normalize_column_name(name: str) -> str:
    return "".join(ch.lower() for ch in name if ch.isalnum())


def _find_column(df: pd.DataFrame, candidates: Iterable[str]) -> Optional[str]:
    normalized = {_normalize_column_name(col): col for col in df.columns}
    for candidate in candidates:
        key = _normalize_column_name(candidate)
        if key in normalized:
            return normalized[key]
    return None


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    date_cols = [col for col in df.columns if "date" in col.lower()]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    for col_name in ["Category", "Sub-Category", "Segment", "Region", "Ship Mode"]:
        col = _find_column(df, [col_name])
        if col:
            df[col] = df[col].astype("string").str.strip()

    num_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = [col for col in df.columns if col not in num_cols and col not in date_cols]

    for col in num_cols:
        median = df[col].median()
        df[col] = df[col].fillna(median)

    for col in cat_cols:
        mode = df[col].mode(dropna=True)
        fill_value = mode.iloc[0] if not mode.empty else "Unknown"
        df[col] = df[col].fillna(fill_value)

    for col in date_cols:
        if df[col].isna().any():
            non_na = df[col].dropna()
            if not non_na.empty:
                df[col] = df[col].fillna(non_na.median())

    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    order_col = _find_column(df, ["Order Date", "Order_Date", "order_date"])
    ship_col = _find_column(df, ["Ship Date", "Ship_Date", "ship_date"])

    if order_col:
        df[order_col] = pd.to_datetime(df[order_col], errors="coerce")
        df["order_month"] = df[order_col].dt.month
        df["order_dayofweek"] = df[order_col].dt.dayofweek

    if order_col and ship_col:
        df[ship_col] = pd.to_datetime(df[ship_col], errors="coerce")
        df["shipping_delay"] = (df[ship_col] - df[order_col]).dt.days

    if not order_col and not ship_col:
        sales_col = _find_column(df, ["Sales"])
        qty_col = _find_column(df, ["Quantity"])
        discount_col = _find_column(df, ["Discount"])
        profit_col = _find_column(df, ["Profit"])

        if sales_col and qty_col:
            sales = pd.to_numeric(df[sales_col], errors="coerce")
            qty = pd.to_numeric(df[qty_col], errors="coerce").clip(lower=1)
            df["sales_per_item"] = sales / qty

        if sales_col and discount_col:
            sales = pd.to_numeric(df[sales_col], errors="coerce")
            discount = pd.to_numeric(df[discount_col], errors="coerce")
            df["discounted_sales"] = sales * (1 - discount)

        if profit_col and sales_col:
            profit = pd.to_numeric(df[profit_col], errors="coerce")
            sales = pd.to_numeric(df[sales_col], errors="coerce").replace(0, pd.NA)
            df["profit_margin"] = (profit / sales).fillna(0)

        if discount_col:
            discount = pd.to_numeric(df[discount_col], errors="coerce")
            df["is_high_discount"] = (discount >= 0.3).astype(int)

    return df


def save_processed(df: pd.DataFrame, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def report_outliers(df: pd.DataFrame) -> None:
    num_cols = df.select_dtypes(include="number").columns.tolist()
    if not num_cols:
        print("Outlier report (IQR): no numeric columns found")
        return

    print("Outlier report (IQR):")
    for col in num_cols:
        series = pd.to_numeric(df[col], errors="coerce").dropna()
        if series.empty:
            continue
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        if iqr == 0:
            outliers = 0
        else:
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr
            outliers = int(((series < lower) | (series > upper)).sum())
        total = len(series)
        ratio = outliers / total * 100
        print(f"  {col}: {ratio:.2f}% ({outliers}/{total})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean and featurize raw data")
    parser.add_argument("--input", required=True, help="Path to raw CSV")
    parser.add_argument(
        "--output",
        default=str(Path("data") / "processed" / "clean.csv"),
        help="Path to save processed CSV",
    )
    args = parser.parse_args()

    df = load_raw(args.input)
    df = clean_data(df)
    df = feature_engineering(df)
    report_outliers(df)
    save_processed(df, args.output)

    print(f"Saved processed data to {args.output}")


if __name__ == "__main__":
    main()
