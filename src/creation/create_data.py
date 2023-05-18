import pandas as pd
from typing import Any
from sklearn.datasets import load_iris
import random


cat_value = ['A', 'B', 'C']  # TODO params for input
target_name = 'target'  # TODO params for input
cat_features = ['cat1']  # TODO params for input


def random_cat_value(cat_value):
    return cat_value[random.randint(a=0, b=len(cat_value)-1)]


def create_data(params: dict[str, Any]):
    data_iris = load_iris()
    feature_names = data_iris['feature_names']  # TODO params for output
    data = pd.DataFrame(data=data_iris['data'], columns=feature_names)
    data[target_name] = data_iris['target']
    for cat in cat_features:
        data[cat] = [random_cat_value(cat_value=cat_value) for _ in range(data.shape[0])]
    data_params = {
        'feature_list': feature_names,
    }
    return {'output': data, 'report': data_params}


def saver_data(data: pd.DataFrame, output: str):
    pd.to_pickle(data, output)


def execute(params: dict[str, Any]) -> dict[str, Any] | None:
    created = create_data(params)  # TODO open params
    saver_data(created['output'], params.get('output'))
    return created.get('report', None)


if __name__ == "__main__":
    execute(params={'output': 'data/raw/data.pickle'})
