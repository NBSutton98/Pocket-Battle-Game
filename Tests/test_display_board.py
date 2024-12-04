from unittest import TestCase
from characters import make_monster
from board import display_map
from unittest.mock import patch
import io


class TestDisplayMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_start(self, mock_stdout):
        board = {(row, col): f"Room at ({row}, {col})" for row in range(5) for col in range(5)}
        name = 'nick'
        monster = make_monster(name)
        monster["x-coordinate"] = 1
        monster["y-coordinate"] = 1
        display_map(board, monster, 5, 5)
        actual = mock_stdout.getvalue()
        expected = (
            "- - - - -\n"
            "- X - - -\n"
            "- - - - -\n"
            "- - - - -\n"
            "- - - - -\n\n"
        )
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_map_middle(self, mock_stdout):
        board = {(row, col): f"Room at ({row}, {col})" for row in range(5) for col in range(5)}
        name = 'nick'
        monster = make_monster(name)
        monster["x-coordinate"] = 2
        monster["y-coordinate"] = 3
        display_map(board, monster, 5, 5)
        actual = mock_stdout.getvalue()
        expected = (
            "- - - - -\n"
            "- - - - -\n"
            "- - - - -\n"
            "- - X - -\n"
            "- - - - -\n\n"
        )
        self.assertEqual(actual, expected)
