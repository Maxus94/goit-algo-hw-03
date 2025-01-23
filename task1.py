import sys, shutil
from pathlib import Path

def search_tree(path: Path) -> None:    

    if path.is_dir():
        for child in path.iterdir():
            search_tree(child)
    else:
        copy_file(dir_target, path)       

def copy_file(path: Path, file_name: Path):
    
    if not path.exists():
        path.mkdir(parents=False, exist_ok=True)
    
    [_, ext]= str(file_name.name).split('.')
    dir_to_copy = Path(ext)
    directory = Path(str(path.name) + '/' + ext)    
    
    if dir_to_copy not in path.iterdir():    
        directory.mkdir(parents=False, exist_ok=True)   
    
    shutil.copy(file_name, directory)

dir_source = Path(sys.argv[1])
dir_target = Path(sys.argv[2]) if len(sys.argv) > 2  else Path("dist")

search_tree(dir_source)
