import inquirer
from read_from_file import read_from_file
from write_to_file import write_to_file_nano
from config import ABS_DIRNAME
import subprocess

option_1 = "Write into a file"
option_2 = (
    "Read from a file (if too big you can choose how many lines to read at a time)"
)

choices = [
    str(option_1),
    str(option_2),
]

# For user prompts Inquirer is being used.
# Docs: https://python-inquirer.readthedocs.io/en/latest/
questions = [
    inquirer.List("main_menu", message="What are you trying to do?", choices=choices)
]

prompt = inquirer.prompt(questions=questions)
answer = prompt["main_menu"]

match answer:
    case answer if answer == option_1:
        write_to_file_nano(ABS_DIRNAME)
    case answer if answer == option_2:
        read_from_file(ABS_DIRNAME)
