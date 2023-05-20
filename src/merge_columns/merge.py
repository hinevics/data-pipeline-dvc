from typing import Any
import pandas as pd


def mergeer(features: list[str], merge_output: str):
    datas = [pd.read_pickle(f) for f in features]
    merge_data = pd.concat(datas, axis=1)
    merge_data.to_pickle(merge_output)


def execute(params: dict[str, Any]) -> dict[str, Any] | None:
    feature_output: list[str] = params.get('feature_output')
    output = params.get('output')
    mergeer(features=feature_output, merge_output=output)
