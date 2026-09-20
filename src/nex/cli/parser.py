import argparse
from nex.core.init import initialize
from nex.core.add import adjoin


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

    # add command
    add_subparser = subparser.add_parser(
        "add", help="Add file contents to the index"
    )
    add_subparser.add_argument(
        "filename", type = str
    )
    add_subparser.set_defaults(func=adjoin)

    return parser