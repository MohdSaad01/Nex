from pathlib import Path
import hashlib
import json

def document(message, **kwargs):
    msg = read_index(message)
    hash_value = hash_message(msg)
    update_head(hash_value)

def read_index(message):
    path = Path(".nex/index")
    data = path.read_text().replace("\n", "")
    msg = {"message":message,"files":data}

    return msg


def hash_message(msg):
    json_string = (json.dumps(msg, indent=4)).encode("utf-8")

    hash_value = hashlib.sha256(json_string).hexdigest()

    prefix = hash_value[:2]
    remainder = hash_value[2:]

    object_dir = Path(".nex") / "objects" / prefix
    object_dir.mkdir(parents=True, exist_ok=True)

    object_file = object_dir / remainder
    object_file.write_bytes(json_string)

    return hash_value


def update_head(hash_value):
    head = Path(".nex/HEAD")
    head.write_text(hash_value)

