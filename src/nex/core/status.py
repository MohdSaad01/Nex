# This will be the implementation of the nex status

from pathlib import Path
import json

def status():
    ih_path = get_path()

    compare_path()



def get_path():
    nex_repo = Path(".nex")

    #HEAD
    head_ref = (nex_repo / "HEAD").read_text()
    head_dict = json.loads((nex_repo / "objects" / head_ref[:2] / head_ref[2:]).read_text())


    #Index
    index_dict = json.loads((nex_repo / "index").read_text())

    return head_dict["files"].keys() | index_dict.keys()

def compare_path():
    ...