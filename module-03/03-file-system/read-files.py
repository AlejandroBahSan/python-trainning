from io import open
import pathlib

route = str(pathlib.Path().absolute()) + "/file_system.md"
file_read = open(route, "r")

content = file_read.read()

print(content)

file_read.close()
