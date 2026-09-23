from pathlib import Path

def adjoin(filename, **kwargs):

    search_dir = Path("../../../")

    file_exits = any(search_dir.rglob(filename))

    if file_exits:
        if check_ignore(filename):
            print("Hashing it")
        else:
            print("File in .nexignore")
    else:
        print("File doesn't exits")

def check_ignore(filename):
    ignore = ".nexignore"

    temp_ignore = Path(ignore).read_text(encoding="utf-8").splitlines()

    ignored_list = []
    for line in temp_ignore:
        if not line.startswith("#") and len(line) > 0:
            ignored_list.append(line)

    if filename not in ignored_list:
        return True

    return None
