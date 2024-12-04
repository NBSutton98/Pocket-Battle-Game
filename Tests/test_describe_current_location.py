from unittest import TestCase
from unittest.mock import patch
import board


class Test(TestCase):
    @patch('random.choice', side_effect=["A cozy studio with a warm fireplace and vintage decor."])
    def test_describe_current_location_start(self, _):
        test_board = board.make_board(1, 1)
        character = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        actual = board.describe_current_location(test_board, character)
        expected = "A cozy studio with a warm fireplace and vintage decor."
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["A colorful child's playroom filled with toys and whimsical murals.",
                                         "A spacious laundry room with organized shelves and a utility sink.",
                                         "A cozy corner in the basement with a plush rug and soft lighting.",
                                         "A tranquil meditation room with soft cushions and calming decor."])
    def test_describe_current_location_board_size(self, _):
        test_board = board.make_board(2, 2)
        character = {"x-coordinate": 1, "y-coordinate": 1, "current_hp": 5}
        actual = board.describe_current_location(test_board, character)
        expected = "A tranquil meditation room with soft cushions and calming decor."
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["A colorful child's playroom filled with toys and whimsical murals.",
                                         "A spacious laundry room with organized shelves and a utility sink.",
                                         "A cozy corner in the basement with a plush rug and soft lighting.",
                                         "A tranquil meditation room with soft cushions and calming decor."])
    def test_describe_current_location_character_position(self, _):
        test_board = board.make_board(2, 2)
        character = {"x-coordinate": 1, "y-coordinate": 1, "current_hp": 5}
        actual = board.describe_current_location(test_board, character)
        expected = "A tranquil meditation room with soft cushions and calming decor."
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["A colorful child's playroom filled with toys and whimsical murals.",
                                         "A spacious laundry room with organized shelves and a utility sink.",
                                         "A cozy corner in the basement with a plush rug and soft lighting.",
                                         "A tranquil meditation room with soft cushions and calming decor."])
    def test_describe_current_location_character_x_position(self, _):
        test_board = board.make_board(2, 2)
        character = {"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5}
        actual = board.describe_current_location(test_board, character)
        expected = "A spacious laundry room with organized shelves and a utility sink."
        self.assertEqual(expected, actual)
