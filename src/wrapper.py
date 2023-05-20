import pandas as pd
from argparse import Namespace
from argdecorators import argparser_wrapper
from utils import get_params, get_named_params


def wrapper(func, params):
    df: pd.DataFrame = pd.read_pickle(params['input'])
    df = func(df, params)
    df.to_pickle(params['output'])
    return df


def feature_wrapper(func):
    @argparser_wrapper
    def inner(arg: Namespace):
        params = get_params(arg.params) if arg.params else {}
        config = get_params(arg.config) if arg.config else {}
        additional = get_params(arg.additional) if arg.additional else {}
        report = get_params(arg.report) if arg.report else {}
        named_arguments = get_named_params(
            ('input', arg.input),
            ('output', arg.output),
            ('feature', arg.feature)
        )
        params.update(config)
        params.update(additional)
        params.update(report)
        params.update(named_arguments)
        wrapper(func, params)
    return inner
