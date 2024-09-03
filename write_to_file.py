import subprocess

from inquirer.themes import GreenPassion
from util.file_utils import prompt_file_selection
import inquirer
from colorama import Fore

PROMPT_KEY = "prompt_response"


def write_to_file(ABS_DIRNAME: str):
    """
    Opens a user-selected file in the Nano editor for editing.

    Args:
        ABS_DIRNAME (str): Absolute directory path where files are located.

    See also:
        subprocess.run: Allows to run commands in the CML
        inquirer: For user prompts Inquirer is being used.
                  Docs: https://python-inquirer.readthedocs.io/en/latest/
    """

    option_1 = "Write new file (.txt supported only)"
    option_2 = "Edit existing file"

    prompt = [
        inquirer.List(
            PROMPT_KEY,
            message="Would you like to edit a file or write a new one? (only .txt files are supported when writing a new one)",
            choices=[option_1, option_2],
        )
    ]

    answer = inquirer.prompt(questions=prompt, theme=GreenPassion())
    answer = answer[PROMPT_KEY]

    match answer:
        case answer if answer == option_1:
            _create_and_edit_file()
        case answer if answer == option_2:
            _edit_file(ABS_DIRNAME=ABS_DIRNAME)


def _edit_file(ABS_DIRNAME: str):
    """
    Allows the user to pick a file from the absolute directory name of the project and opens it on nano.

    Args:
        ABS_DIRNAME (str): absolute directory name where all files are pulled from.

    See also:
        subprocess.run: Allows to run commands in the CML
                        Docs: https://docs.python.org/3/library/subprocess.html#subprocess.run
        nano: Command line text editor - here it's being used to edit a file right after its creationg
              Docs: https://www.nano-editor.org/docs.php
    """

    file_path = prompt_file_selection("What file do you want to edit? ", ABS_DIRNAME)

    subprocess.run(
        [
            "nano",
            file_path,
        ]
    )


def _create_and_edit_file():
    """
    Allows the user to create and edit a file.

    This function prompts the user for a file name and path name. If the file creating succeeds
    the file is then opened in nano. Otherwise, the user is asked to input a valid file and path name

    See also:
        subprocess.run: Allows to run commands in the CML
        nano: Command line text editor - here it's being used to edit a file right after its creationg
              Docs: https://www.nano-editor.org/docs.php
        colorama: Used to accentuate certain lines in the terminal
                  Docs: https://pypi.org/project/colorama/
        inquirer: For user prompts Inquirer is being used.
                  Docs: https://python-inquirer.readthedocs.io/en/latest/
    """
    while True:

        filname_prompt = [
            inquirer.Text(
                PROMPT_KEY,
                message="What do you want to name your file? (no extensions allowed)",
            )
        ]

        filename_prompt_answer = inquirer.prompt(filname_prompt, theme=GreenPassion())
        filename_prompt_answer: str = filename_prompt_answer[PROMPT_KEY]

        filename: str = ""
        for part in filename_prompt_answer.split("."):
            if part != ".":
                filename += part

        # Only .txt files supported for now
        filename = filename + ".txt"

        print(
            Fore.CYAN
            + "\nAbsolute path example (macOS): /Users/<username>/Documents/coding/cs-128/file-reader-writer"
            + "\nAbsolute path example (windows): C:/Users/<username>/Documents/coding/cs-128/file-reader-writer"
            + "\nRelative path example: util"
        )
        pathname_prompt = [
            inquirer.Text(
                PROMPT_KEY,
                message="Please type the absolute/relative path where you want to save this file",
            )
        ]

        pathname_prompt_answer: str = inquirer.prompt(pathname_prompt)
        pathname = pathname_prompt_answer[PROMPT_KEY] + f"/{filename}"

        try:
            with open(pathname, "w") as f:
                pass
            break
        except FileNotFoundError:
            print(
                Fore.RED
                + f"\nOops! Something went wrong. It seems like your pathname/filename is invalid. "
            )
            print(
                Fore.CYAN
                + "\nFile name example: example_file"
                + "\nAbsolute path name example (macOS): /Users/<username>/Documents/coding/cs-128/file-reader-writer"
                + "\nAbsolute path example (windows): C:/Users/<username>/Documents/coding/cs-128/file-reader-writer"
                + "\nRelative path example file-reader-writer/util"
            )

            print(
                Fore.CYAN
                + f"\nYour file path: {pathname}"
                + f"\nYour file name: {filename}"
                + "\n"
            )

    subprocess.run(["nano", pathname])
