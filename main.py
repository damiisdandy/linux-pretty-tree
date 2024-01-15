import typer
from typing import Optional, Annotated
import os
from utils import (
    CHARACTERS,
    display_indent_ui,
    get_last_index,
    get_dirs_in_folder,
    get_parent_dir,
)


app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(folder_path: Annotated[Optional[str], typer.Argument()] = None):
    """List nested file tree in a pretty way :)"""
    folder_path = folder_path or os.getcwd()
    absolute_path = os.path.abspath(folder_path)
    if not os.path.exists(absolute_path):
        print(f"Path does not exist {CHARACTERS.BAD}")
        return
    # sort by directory first
    walked_dirs_files = []
    for root, dirs, files in os.walk(absolute_path):
        if f"{os.sep}." in root:
            continue
        dirs.sort()
        files.sort()
        walked_dirs_files.append((root, dirs, files))

    walked_dirs_files.sort(key=lambda x: x[0])

    for root, dirs, files in walked_dirs_files:
        dir_name = os.path.basename(root)
        # sort files
        files.sort()
        level = root.replace(absolute_path, "").count(os.sep)
        # skip root directory
        if root != absolute_path:
            parent_dir = get_parent_dir(root)
            dirs_in_parent = get_dirs_in_folder(parent_dir)
            dirs_in_parent.sort()

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


if __name__ == "__main__":
    app()
