from __future__ import annotations

from math import sqrt
from typing import Dict

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def compute_mae(y_true, y_pred) -> float:
    return mean_absolute_error(y_true, y_pred)


def compute_rmse(y_true, y_pred) -> float:
    return sqrt(mean_squared_error(y_true, y_pred))


def compute_r2(y_true, y_pred) -> float:
    return r2_score(y_true, y_pred)


def evaluate_regression(y_true, y_pred) -> Dict[str, float]:
    return {
        "mae": compute_mae(y_true, y_pred),
        "rmse": compute_rmse(y_true, y_pred),
        "r2": compute_r2(y_true, y_pred),
    }
