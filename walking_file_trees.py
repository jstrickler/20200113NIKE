#!/usr/bin/env python
import os

START = "."
# START = os.path.abspath(START)

for curr_dir, folders, files in os.walk(START):
    if '.git' in folders:
        folders.remove('.git')
    print(curr_dir)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print("    {:6d} {}".format(file_size, file_name))


