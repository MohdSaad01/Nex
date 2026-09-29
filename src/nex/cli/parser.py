import argparse
from nex.core.init import initialize
from nex.core.add import adjoin
from nex.core.commit import document
from nex.core.status import status


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
    add_subparser.set_defaults(func = adjoin)

    # commit subparser
    commit_subparser = subparser.add_parser(
        "commit", help = "Record changes to the repository"
    )
    commit_subparser.add_argument(
        "-m", dest="message"
    )
    commit_subparser.set_defaults(func = document)

    # status command
    status_subparser = subparser.add_parser(
        "status", help="Show the working tree status"
    )
    status_subparser.set_defaults(func=status)

    return parser