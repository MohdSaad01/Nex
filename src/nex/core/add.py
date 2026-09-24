import json
from pathlib import Path
import hashlib

def adjoin(filename, **kwargs):

    search_dir = Path("../../../")

    file_exits = any(search_dir.rglob(filename))

    if file_exits:
        if check_ignore(filename):
            print("Hashing File...")
            hash_file(filename)
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

def hash_file(filename):
    path = Path(filename)
    data = path.read_bytes()

    hash_value = hashlib.sha256(data).hexdigest()

    prefix = hash_value[:2]
    remainder = hash_value[2:]

    object_dir = Path(".nex") / "objects" / prefix
    object_dir.mkdir()

    object_file = object_dir / remainder
    object_file.write_bytes(data)

    update_index(filename, hash_value)

def update_index(filename, hash_value):
    index_path = Path(".nex/index")
    index = {}

    if index_path.exists():
        index = json.loads(index_path.read_text())

    index[filename] = hash_value
    index_path.write_text(json.dumps(index, indent = 2))