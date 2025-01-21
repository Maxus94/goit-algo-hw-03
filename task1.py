import sys
from pathlib import Path

def display_tree(path: Path, indent: str = "") -> None:
    print(indent + str(path.name))

    if path.is_dir():
        for child in path.iterdir():
            display_tree(child, indent + "    ")


dir_source = sys.argv[1]
dir_target = sys.argv[2] if len(sys.argv) > 2  else "dist"



print(dir_source)
print(dir_target)
