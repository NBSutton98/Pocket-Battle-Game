from unittest import TestCase
from unittest.mock import patch
import board


class Test(TestCase):
    @patch('random.choice', side_effect=["A cozy studio with a warm fireplace and vintage decor."])
    def test_make_board_smallest(self, _):
        actual = board.make_board(1, 1)
        expected = {(0, 0): "A cozy studio with a warm fireplace and vintage decor."}
        self.assertEqual(actual, expected)

    @patch('random.choice', side_effect=["A colorful child's playroom filled with toys and whimsical murals.",
                                         "A spacious laundry room with organized shelves and a utility sink.",
                                         "A cozy corner in the basement with a plush rug and soft lighting.",
                                         "A tranquil meditation room with soft cushions and calming decor."])
    def test_make_board_big(self, _):
        actual = board.make_board(2, 2)
        expected = {(0, 0): "A colorful child's playroom filled with toys and whimsical murals.",
                    (0, 1): 'A spacious laundry room with organized shelves and a utility sink.',
                    (1, 0): 'A cozy corner in the basement with a plush rug and soft lighting.',
                    (1, 1): 'A tranquil meditation room with soft cushions and calming decor.'}
        self.assertEqual(actual, expected)
