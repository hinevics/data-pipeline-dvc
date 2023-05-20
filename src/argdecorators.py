import argparse


def argparser_wrapper(handle):  # TODO переиеновать его тк я его использую как парсер I/O
    def wrapper():
        parser = argparse.ArgumentParser(
            description="This is a pipeline for model training",
        )
        parser.add_argument(
            '-p',
            '--params',
            help='Path to the stage parameters',
            type=str,
            default=None
            )
        parser.add_argument(
            '-a',
            '--additional',
            help='Path to the additional parameters',
            type=str,
            default=None
            )
        parser.add_argument(
            '-c',
            '--config',
            help='Path to the config parameters',
            type=str,
            default=None
            )
        parser.add_argument(
            '-r',
            '--report',
            help='Path to the report parameters',
            type=str,
            default=None
            )
        parser.add_argument(
            '-i',
            '--input',
            help='Input data',
            type=str,
            default=None
        )
        parser.add_argument(
            '-o',
            '--output',
            help='Output data',
            type=str,
            default=None
        )
        parser.add_argument(
            '-f',
            '--feature',
            help='Name feature for run',
            type=str,
            default=None
        )
        parser.set_defaults(callback=handle)
        args = parser.parse_args()
        args.callback(args)
    return wrapper
