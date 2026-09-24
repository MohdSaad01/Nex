from pathlib import Path
import subprocess

def initialize():

    nex_path = Path.cwd() / ".nex"

    try:
        nex_path.mkdir()

        subprocess.run(
            ["attrib", "+h", str(nex_path)],
            check = True
        )

        initialize_repo(nex_path)

        print(f"Initialized empty Nex repository in {nex_path}")

    except FileExistsError:
        # If someone ran the **init** command twice or if there is already a same name folder then git reads the config, objects and other related file to actually confirm that it is a real .git repo, it also pulls new template files without overwriting.
        # I didn't implement those concepts because they would have been too complex for the project. I just checked for the .nex folder to actually confirm the repo, and if there is a .nex folder, then if it is empty I delete it and then initialize a new one or if it is not empty I just reinitialize without further checking.

        if nex_path.is_file():
            nex_path.unlink()
            initialize()
        elif nex_path.is_dir() and not any(nex_path.iterdir()):
            nex_path.rmdir()
            initialize()
        else:
            print(f"Reinitialized existing Nex repository in {nex_path}")

    except PermissionError:
        print(f"Permission denied: Unable to create '{nex_path}'. Please grant the required permission")

    except Exception as e:
        print(f"An error occurred: {e}")

def initialize_repo(directory_path):

    #objects
    objects_path = directory_path / "objects"
    objects_path.mkdir()

    #refs
    refs_path = directory_path / "refs"
    refs_path.mkdir()

    refs_head = refs_path / "heads"
    refs_head.mkdir()

    main_head = refs_head / "main"
    main_head.touch()

    #HEAD
    head_path = directory_path / "HEAD"
    head_path.write_text("ref: refs/heads/main")

    #index
    index_path = directory_path / "index"
    index_path.write_text("{}")
