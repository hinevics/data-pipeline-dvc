import os
import sys
from typing import Any
import pandas as pd
import numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from wrapper import feature_wrapper  # noqa E402


def update_features(x: float):
    return np.log10(x + x)


@feature_wrapper
def sepal_width(df: pd.DataFrame | None = None,
                params: dict[str, Any] | None = None) -> pd.DataFrame:
    feature = params.get('feature')
    df = df[[feature]].copy()
    return df


if __name__ == "__main__":
    sepal_width()
