import typer
from typing import Optional, Annotated
import os

from logic import print_tree_non_recursive
from utils import CHARACTERS


app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(folder_path: Annotated[Optional[str], typer.Argument()] = None):
    """List nested file tree in a pretty way :)"""
    folder_path = folder_path or os.getcwd()
    absolute_path = os.path.abspath(folder_path)
    if not os.path.exists(absolute_path):
        print(f"Path does not exist {CHARACTERS.BAD}")
        return
    print_tree_non_recursive(absolute_path)


if __name__ == "__main__":
    app()
