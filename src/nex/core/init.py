from pathlib import Path
import subprocess

def initialize():

    directory_path = Path.cwd() / ".nex"

    try:
        directory_path.mkdir()

        subprocess.run(
            ["attrib", "+h", str(directory_path)],
            check = True
        )

        print(f"Initialized empty Nex repository in {directory_path}")

    except FileExistsError:
        # If someone ran the **init** command twice or if there is already a same name folder then git reads the config, objects and other related file to actually confirm that it is a real .git repo, it also pulls new template files without overwriting.
        # I didn't implement those concepts because they would have been too complex for the project. I just checked for the .nex folder to actually confirm the repo, and if there is a .nex folder, then if it is empty I delete it and then initialize a new one or if it is not empty I just reinitialize without further checking.

        if directory_path.is_file():
            directory_path.unlink()
            initialize()
        elif directory_path.is_dir() and not any(directory_path.iterdir()):
            directory_path.rmdir()
            initialize()
        else:
            print(f"Reinitialized existing Nex repository in {directory_path}")

    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_path}'. Please grant the required permission")

    except Exception as e:
        print(f"An error occurred: {e}")
