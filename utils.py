import os
from typing import Any
from settings import INDENT_SIZE, INDENT_HORIZONAL_LENGTH


class CHARACTERS:
    BAD: str = "❌"
    GOOD: str = "✅"
    FOLDER: str = "📁 "
    FILE: str = "📄 "
    INDENT_BAR_START: str = "\x1b(0\x74\x1b(B"
    INDENT_BAR_VERTICAL: str = "\x1b(0\x6d\x1b(B"
    INDENT_BAR_VERTICAL_LONG = "\x1b(0\x78\x1b(B"
    INDENT_BAR_HORIZONTAL: str = "\x1b(0\x71\x1b(B"


def get_last_index(iterable: list[Any]):
    return iterable.index(iterable[-1])


def display_indent_ui(level: int, is_last_item: bool = False):
    indent_space = INDENT_SIZE * level
    indent_ui_start = (
        CHARACTERS.INDENT_BAR_VERTICAL if is_last_item else CHARACTERS.INDENT_BAR_START
    )
    indent_ui_body = CHARACTERS.INDENT_BAR_HORIZONTAL * INDENT_HORIZONAL_LENGTH
    indent_ui = indent_ui_start + indent_ui_body + " "
    return (" " * indent_space) + indent_ui


def get_dirs_in_folder(folder_path: str):
    dirs_output = []
    for dir in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, dir)):
            dirs_output.append(dir)
    return dirs_output


def get_parent_dir(folder_path: str):
    return os.path.normpath(folder_path + os.sep + os.pardir)
  

def join_parent_opposing_dir_ui(root_path: str, folder_path: str):
    
