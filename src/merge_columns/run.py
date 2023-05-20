import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from argparse import Namespace  # noqa E402
from argdecorators import argparser_wrapper  # noqa E402
from utils import get_params, get_named_params, give_params  # noqa E402
from merge import execute  # noqa E402


@argparser_wrapper
def runer(arg: Namespace):
    params = get_params(arg.params) if arg.params else {}
    config = get_params(arg.config) if arg.config else {}
    additional = get_params(arg.additional) if arg.additional else {}
    named_arguments = get_named_params(
        ('input', arg.input), ('output', arg.output)
    )
    params.update(config)
    params.update(additional)
    params.update(named_arguments)
    report = execute(params)
    if report:
        give_params(arg.report, report)


if __name__ == "__main__":
    runer()
