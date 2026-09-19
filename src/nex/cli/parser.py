import argparse
from nex.core.init import initialize


def create_parser():
    parser = argparse.ArgumentParser(
        description = "A Nex cli parser"
    )

    subparser = parser.add_subparsers(
        dest= "command"
    )

    # init command
    init_subparser = subparser.add_parser(
        "init", help = "Create an empty Git repository or reinitialize an existing one"
    )
    init_subparser.set_defaults(func = initialize)

    return parser