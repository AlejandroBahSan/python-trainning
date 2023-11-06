from io import open
import pathlib
import shutil

original_route = str(pathlib.Path().absolute()) + "/file_system.md"
new_route = str(pathlib.Path().absolute()) + "/new_file_system.md"

shutil.copyfile(original_route, new_route)
