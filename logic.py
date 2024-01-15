from utils import (
    CHARACTERS,
    display_indent_ui,
    get_last_index,
    get_dirs_in_folder,
    get_parent_dir,
)
import os


def print_tree_non_recursive(folder_path: str):
    """Prints the tree structure of a given path (non-recursively)."""
    # sort by directory first
    walked_dirs_files = [
        (root, dirs, files) for root, dirs, files in os.walk(folder_path)
    ]
    walked_dirs_files.sort(key=lambda x: x[0])

    for root, dirs, files in walked_dirs_files:
        # sort files
        files.sort()
        level = root.replace(folder_path, "").count(os.sep)
        # skip root directory
        if root != folder_path:
            parent_dir = get_parent_dir(root)
            dirs_in_parent = get_dirs_in_folder(parent_dir)
            dirs_in_parent.sort()
            dir_name = os.path.basename(root)
            is_last_dir = dir_name == dirs_in_parent[-1]
            print(
                f"{display_indent_ui(level=level - 1, is_last_item=is_last_dir)}{CHARACTERS.FOLDER}{dir_name}/"
            )
        for index, file in enumerate(files):
            is_last_file_index = index == get_last_index(files)
            # no more directories come after files
            is_last_file = is_last_file_index and not dirs
            print(
                f"{display_indent_ui(level=level, is_last_item=is_last_file)}{CHARACTERS.FILE}{file}"
            )


def print_tree_recursive(folder_path: str):
    """Prints the tree structure of a given path (recursively)."""
    pass
