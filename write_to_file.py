import subprocess
from util.file_utils import prompt_file_selection


def write_to_file_nano(ABS_DIRNAME: str):
    """
    Opens a user-selected file in the Nano editor for editing.

    Args:
        ABS_DIRNAME (str): Absolute directory path where files are located.

    See also:
        subprocess.run: Allows to run commands in the CML
        nano: Command line text editor
    """

    file_path = prompt_file_selection("What file do you want to edit? ", ABS_DIRNAME)

    subprocess.run(
        [
            "nano",
            file_path,
        ]
    )
