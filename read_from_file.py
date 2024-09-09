from util.file_utils import prompt_file_selection, is_file_size_exceeded
from config import FILE_SIZE_THRESHOLD
from colorama import Fore


def read_from_file(ABS_DIRNAME: str):
    """
    Reads and prints a file of the user's choice in the specified directory.

    Given an absolute directory path, all files are extracted no matter how nested into many directories.
    The user is allowed to make the choice of which file to read.

    If the file size is greater than FILE_SIZE_THRESHOLD, the content is printed 5 lines at a time.

    Args:
        ABS_DIRNAME (str): Absolute directory path where files are located

    See also:
        colorama: Used to accentuate certain lines in the terminal
                  docs: https://pypi.org/project/colorama/
    """

    requested_file_path = prompt_file_selection(
        "What file do you want to read from?", ABS_DIRNAME
    )

    is_file_too_big = is_file_size_exceeded(
        abs_filepath=requested_file_path, threshold=FILE_SIZE_THRESHOLD
    )

    with open(requested_file_path, "r") as f:
        if not is_file_too_big:

            file_name = requested_file_path.split("/")[-1]

            # Split the file path by "/"s and grab the last one (the file title)
            print(Fore.CYAN + f"File name: {file_name}" + "\n\n")
            print(Fore.CYAN + f.read() + "\n")

        lines = []

        while line := f.readline():

            if len(lines) >= 5:
                for line in lines:
                    print(Fore.CYAN + line)

                wants_to_continue = input(
                    Fore.BLUE
                    + 'Print next 5 lines? ("enter to continue" or "n" to cancel): '
                )
                if wants_to_continue == "n":
                    return

                lines = []

                # If len(lines) > 5, we want to read another line at the end.
                #  Otherwise the last read line will be pushed to lines
                line = f.readline()

            if repr("\n") != repr(line):
                lines.append(line)
