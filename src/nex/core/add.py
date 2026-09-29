import json
from pathlib import Path
import hashlib

def adjoin(filename, **kwargs):

    search_dir = Path("C:/Zeus/Nex/")

    search_results = search_dir.rglob(filename)
    file_path = next(search_results, None)

    if file_path is not None:
        if check_ignore(filename):
            hash_file(file_path)
            print(f"Added '{filename}' to staging area")
        else:
            print(f"'{filename}' is ignored by .nexignore")
    else:
        print(f"fatal: pathspec '{filename}' did not match any files")

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

def hash_file(filename):
    path = Path(filename)
    data = path.read_bytes()

    hash_value = hashlib.sha256(data).hexdigest()

    prefix = hash_value[:2]
    remainder = hash_value[2:]

    object_dir = Path(".nex") / "objects" / prefix
    object_dir.mkdir(parents=True, exist_ok=True)

    object_file = object_dir / remainder
    object_file.write_bytes(data)

    update_index(filename, hash_value)

def update_index(filename, hash_value):
    index_path = Path(".nex/index")
    index = {}

    if index_path.exists():
        index = json.loads(index_path.read_text())

    relative_path = Path(filename).relative_to(Path.cwd())

    index[str(relative_path)] = hash_value
    index_path.write_text(json.dumps(index, indent = 2))