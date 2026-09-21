from pathlib import Path

def adjoin(filename, **kwargs):

    search_dir = Path("../../../")

    file_exits = any(search_dir.rglob(filename))

    if file_exits:
        print("File exits")
    else:
        print("File doesn't exits")

