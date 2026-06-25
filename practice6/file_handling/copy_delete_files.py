import os

os.remove("textfile.txt") # deletes the file "textfile.txt" from the current directory.

if os.path.exists("textfile.txt"): # checks if the file "textfile.txt" exists in the current directory
  os.remove("textfile.txt")
else:
  print("The file does not exist")

os.rmdir("system32") # deletes the directory "system32" from the current directory.
# Note: You can only remove empty folders.

import shutil
shutil.rmtree("myfolder") # deletes the directory "myfolder" and all its contents from the current directory.

import pathlib
path = pathlib.Path("textfile.txt") # creates a Path object for the file "textfile.txt"
if path.exists(): # checks if the file "textfile.txt" exists in the current directory
    path.unlink() # deletes the file "textfile.txt" from the current directory
