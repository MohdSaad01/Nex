# This will be the implementation of the nex status

from pathlib import Path
import json

def status():
    ih_path,head_dict,index_dict = get_path()


    compare_path(ih_path,head_dict,index_dict)



def get_path():
    nex_repo = Path(".nex")

    #HEAD
    head_ref = (nex_repo / "HEAD").read_text()
    head_dict = json.loads((nex_repo / "objects" / head_ref[:2] / head_ref[2:]).read_text())


    #Index
    index_dict = json.loads((nex_repo / "index").read_text())

    return head_dict["files"].keys() | index_dict.keys(),head_dict["files"],index_dict

def compare_path(all_paths, head_dict, index_dict):
    for path in all_paths:

        if path in head_dict and path in index_dict:
            if head_dict[path] != index_dict[path]:
                print("modified")
            else:
                print("unchanged")

        elif path in index_dict:
            print("added")

        else:
            print("deleted")
