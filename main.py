import typer
from typing import Optional, Annotated
import os
from utils import (
    CHARACTERS,
    display_indent_ui,
    get_last_index,
    get_adjacent_dirs,
    get_icon,
)


app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(
    folder_path: Annotated[Optional[str], typer.Argument()] = None,
    show_hidden_files: bool = False,
):
    """List nested file tree in a pretty way :)"""
    folder_path = folder_path or os.getcwd()
    root_absolute_path = os.path.abspath(folder_path)
    if not os.path.exists(root_absolute_path):
        print(f"Path does not exist {CHARACTERS.BAD}")
        return
    # sort by directory first
    walked_dirs_files = []
    for root, dirs, files in os.walk(root_absolute_path):
        if f"{os.sep}." in root and not show_hidden_files:
            continue
        dirs.sort()
        files.sort()
        walked_dirs_files.append((root, dirs, files))

    # sort by root directory
    walked_dirs_files.sort(key=lambda x: x[0])

    for root, dirs, files in walked_dirs_files:
        dir_name = os.path.basename(root)
        # sort files
        files.sort()
        # skip root directory
        if root != root_absolute_path:
            is_last_dir = get_adjacent_dirs(root)["next"] is None
            print(
                f"{display_indent_ui(root_path=root_absolute_path, path=root, is_last_item=is_last_dir)}{get_icon(root)} {CHARACTERS.boldify(CHARACTERS.orangeify(dir_name))}"
            )
        for index, file in enumerate(files):
            full_file_path = os.path.join(root, file)
            is_last_file_index = index == get_last_index(files)
            # no more directories come after files
            is_last_file = is_last_file_index and not dirs
            print(
                f"{display_indent_ui(root_path=root_absolute_path, path=full_file_path, is_last_item=is_last_file)}{get_icon(file)} {file}"
            )


if __name__ == "__main__":
    app()
