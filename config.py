from os import path

# Absolute path name for the directory this file is within
ABS_DIRNAME = path.dirname(path.abspath(__file__))

# Used at read_from_file.py and passed down to util/file_utils.py as a guide for a file's maximum size
# before it is read 5 lines at a time
FILE_SIZE_THRESHOLD = 1024 * 100
