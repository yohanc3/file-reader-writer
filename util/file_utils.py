from os import walk, stat
import inquirer
from inquirer.themes import GreenPassion


class FileInfo:
    """
    A class representing a file with its path and name.

    Attributes:
        path (str): The full file path.
        name (str): The name of the file.

    Methods:
        __repr__(): Returns a string representation of the file, combining its name and path.
    """

    def __init__(self, path: str, name: str):
        self.path = path
        self.name = name

    def __repr__(self):
        return f"{self.name} - {self.path}"


def all_files_in_dir(dirname: str):
    """
    Retrieve a list of all files in a specified directory and its subdirectories.

    This function traverses the given directory recursively and creates a list of `FileInfo`
    objects representing each file found. The `FileInfo` objects contain the file's path and name.

    Args:
        dirname (str): The path to the directory to search.

    Returns:
        List[FileInfo]: A list of `FileInfo` objects for each file in the directory.

    See Also:
        os.walk: A function used to generate file names in a directory tree by walking either top-down or bottom-up.
                 Docs: https://docs.python.org/3/library/os.html#os.walk
    """

    flattened_files = []

    for root, _, files in walk(dirname):
        for file in files:

            new_file_struct = FileInfo(path=f"{root}/{file}", name=file)
            flattened_files.append(new_file_struct)

    return flattened_files


def prompt_file_selection(message: str, abs_dirpath: str):
    """

    Given a message and absolute directory path,
      this function pulls all files from the directory path and allows the user to pick one.

    Args:
        message (str): Message shown to the user as the initial prompt.
        abs_dirpath (str): Absolute directory path used to pull all file names in the directory and have the user pick one.

    Returns: User-selected file path (str)

    See also:
        inquirer: For user prompts Inquirer is being used.
                  Docs: https://python-inquirer.readthedocs.io/en/latest/
    """

    all_files = all_files_in_dir(abs_dirpath)

    questions = [
        inquirer.List(
            "file_name",
            message=message,
            choices=[file for file in all_files],
        )
    ]

    answer = inquirer.prompt(questions=questions, theme=GreenPassion())

    matched_file = list(filter(lambda file: file == answer["file_name"], all_files))[0]

    matched_file_path = matched_file.path
    return matched_file_path


def is_file_size_exceeded(abs_filepath: str, threshold: int):
    """
    This helper function calculates if a file's size is within a given threshold or not.

    Args:
        abs_filepath (str): Absolute file path
        threshold (int): Represented in bits, it is the maximum size a file can be.

    See also:
        stat(abs_filepath: str).st_size: Given an absolute filepath, it returns the file size in bits
                                         Docs: https://docs.python.org/3/library/stat.html#stat.ST_SIZE
    """

    file_size = stat(abs_filepath).st_size

    if file_size < threshold:
        return False

    return True
