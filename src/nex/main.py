from nex.cli.parser import create_parser

def main():
    parser =  create_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        func = args.func

        kwargs = vars(args).copy()
        del kwargs["func"]

        func(**kwargs)

if __name__ == "__main__":
    main()
