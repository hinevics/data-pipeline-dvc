import os
import sys
from typing import Any
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from wrapper import feature_wrapper  # noqa E402


def update_features(x: float):
    return x * 10


@feature_wrapper
def sepal_length(df: pd.DataFrame | None = None, params: dict[str, Any] | None = None):
    df[params.get('feature')] = df[params.get('feature')].fillna(0)
    df[params.get('feature')] = df[params.get('feature')].map(update_features)


if __name__ == "__main__":
    sepal_length()
