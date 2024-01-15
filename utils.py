import os
from typing import Any
from settings import INDENT_SIZE, INDENT_HORIZONAL_LENGTH


class CHARACTERS:
    BAD: str = "❌"
    GOOD: str = "✅"
    FOLDER: str = "📁"
    FILE: str = "📄"
    PICTURE: str = "🖼️ "
    VIDEO: str = "🎥"
    AUDIO: str = "🎵"
    SPACE = " " * INDENT_SIZE
    SPACE_WITH_PILLAR = "\x1b(0\x78\x1b(B" + (" " * (INDENT_SIZE - 1))
    T_INDENT_UI = (
        "\x1b(0\x74\x1b(B" + ("\x1b(0\x71\x1b(B" * INDENT_HORIZONAL_LENGTH) + " "
    )
    L_INDENT_UI = (
        "\x1b(0\x6d\x1b(B" + ("\x1b(0\x71\x1b(B" * INDENT_HORIZONAL_LENGTH) + " "
    )
    BOLD = "\033[1m"
    CLEAR = "\033[0m"
    ORANGE = "\033[33m"

    def __init__(self):
        pass

    def boldify(string: str):
        return CHARACTERS.BOLD + string + CHARACTERS.CLEAR

    def orangeify(string: str):
        return CHARACTERS.ORANGE + string + CHARACTERS.CLEAR


def get_last_index(iterable: list[Any]):
    return iterable.index(iterable[-1])


def get_dirs_in_folder(folder_path: str):
    dirs_output = []
    for dir in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, dir)):
            dirs_output.append(dir)
    dirs_output.sort()
    return dirs_output


def get_parent_dir(folder_path: str):
    return os.path.normpath(folder_path + os.sep + os.pardir)


def get_adjacent_dirs(folder_path: str):
    folder_path = os.path.abspath(folder_path)
    parent_dir = get_parent_dir(folder_path)
    dirs_in_parent = get_dirs_in_folder(parent_dir)
    current_dir = os.path.basename(folder_path)
    current_dir_index = dirs_in_parent.index(current_dir)
    adjacent_dirs = {
        "previous": None,
        "next": None,
    }
    if current_dir_index > 0:
        # append directory before current directory
        adjacent_dirs["previous"] = dirs_in_parent[current_dir_index - 1]
    if current_dir_index < get_last_index(dirs_in_parent):
        adjacent_dirs["next"] = dirs_in_parent[current_dir_index + 1]
    return adjacent_dirs


def join_parent_opposing_dir_ui(root_path: str, path: str):
    path_nesting = path.replace(root_path, "").split(os.sep)

    output = ""
    for _ in path_nesting:
        parent_dir = get_parent_dir(os.path.join(root_path, *path_nesting))
        has_bottom_dir = get_adjacent_dirs(parent_dir)["next"] is not None
        if parent_dir == root_path:
            continue
        if has_bottom_dir:
            output = CHARACTERS.SPACE_WITH_PILLAR + output
        else:
            output = CHARACTERS.SPACE + output
        path_nesting.pop()

    return output


def display_indent_ui(root_path: str, path: str, is_last_item: bool = False):
    indent_ui = CHARACTERS.L_INDENT_UI if is_last_item else CHARACTERS.T_INDENT_UI
    return join_parent_opposing_dir_ui(root_path, path) + indent_ui


def get_icon(path: str):
    image_extentions = ["jpg", "jpeg", "png", "gif", "svg", "webp", "bmp", "ico"]
    video_extentions = ["mp4", "webm", "ogg", "mov", "flv", "avi", "mkv"]
    audio_extentions = ["mp3", "wav", "ogg", "m4a", "flac", "aac"]
    if os.path.isdir(path):
        return CHARACTERS.FOLDER
    else:
        if path.split(".")[-1].lower() in image_extentions:
            return CHARACTERS.PICTURE
        elif path.split(".")[-1].lower() in video_extentions:
            return CHARACTERS.VIDEO
        elif path.split(".")[-1].lower() in audio_extentions:
            return CHARACTERS.AUDIO
        else:
            return CHARACTERS.FILE
