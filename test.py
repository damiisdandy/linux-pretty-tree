import unittest
from utils import (
    get_last_index,
    get_dirs_in_folder,
    get_parent_dir,
    get_adjacent_dirs,
    join_parent_opposing_dir_ui,
    CHARACTERS,
)
import os


class TestUtilities(unittest.TestCase):
    def test_get_last_index(self):
        self.assertEqual(get_last_index([num for num in range(4)]), 3)
        self.assertEqual(get_last_index([num for num in range(100)]), 99)

    def test_dirs_in_folder(self):
        directory = os.path.abspath(os.path.join(os.getcwd(), "example"))
        self.assertListEqual(
            get_dirs_in_folder(directory),
            ["directory_1", "directory_2", "directory_2_2"],
        )

    def test_get_parent_dir(self):
        directory = os.path.abspath(os.path.join(os.getcwd(), "example"))
        self.assertEqual(
            get_parent_dir(directory), os.path.abspath(os.path.join(os.getcwd()))
        )

    def test_get_adjacent_dirs(self):
        directory = os.path.abspath(os.path.join(os.getcwd(), "example", "directory_2"))
        self.assertDictEqual(
            get_adjacent_dirs(directory),
            {"previous": "directory_1", "next": "directory_2_2"},
        )

    def test_join_parent_opposing_dir_ui(self):
        root_dir = os.path.abspath(os.path.join(os.getcwd()))

        path_nesting = ["example"]
        directory = os.path.join(root_dir, *path_nesting)
        indent_ui = ""
        self.assertEqual(join_parent_opposing_dir_ui(root_dir, directory), indent_ui)

        path_nesting = ["example", "directory_1", "file_1.txt"]
        directory = os.path.join(root_dir, *path_nesting)
        indent_ui = CHARACTERS.SPACE + CHARACTERS.SPACE_WITH_PILLAR
        self.assertEqual(join_parent_opposing_dir_ui(root_dir, directory), indent_ui)

        path_nesting = ["example", "directory_2", "directory_3", "file_3.txt"]
        directory = os.path.join(root_dir, *path_nesting)
        indent_ui = (
            CHARACTERS.SPACE
            + CHARACTERS.SPACE_WITH_PILLAR
            + CHARACTERS.SPACE_WITH_PILLAR
        )

        self.assertEqual(join_parent_opposing_dir_ui(root_dir, directory), indent_ui)


if __name__ == "__main__":
    unittest.main()
