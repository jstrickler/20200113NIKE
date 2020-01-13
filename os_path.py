#!/usr/bin/env python
import os

FOLDER = 'DATA'
FILENAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILENAME)
print("file path:", file_path)

# file_path = os.sep.join([FOLDER, FILENAME])
# print("file path:", file_path)

file_size = os.path.getsize(file_path)
print("file size:", file_size)

file_timestamp_raw = os.path.getmtime(file_path)
print("raw timestamp:", file_timestamp_raw)

from datetime import datetime
file_timestamp = datetime.fromtimestamp(file_timestamp_raw)
print("timestamp:", file_timestamp)


