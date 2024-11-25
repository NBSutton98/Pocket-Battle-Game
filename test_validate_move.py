from unittest import TestCase
from unittest.mock import patch
import game
from game import get_user_choice, make_monster


class Test(TestCase):

    @patch('builtins.input', side_effect=['s'])
    def test_validate_move_up(self, _):
        name = 'nick'
        character = make_monster(name)
        direction = get_user_choice()
        expected = True
        actual = game.validate_move(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['w'])
    def test_validate_move_down(self, _):
        character = {"x-coordinate": 0, "y-coordinate": 1, "current_hp": 5}
        direction = get_user_choice()
        expected = True
        actual = game.validate_move(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['d'])
    def test_validate_move_right(self, _):
        name = 'nick'
        character = make_monster(name)
        direction = get_user_choice()
        expected = True
        actual = game.validate_move(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a'])
    def test_validate_move_left(self, _):
        character = {"x-coordinate": 1, "y-coordinate": 0, "current_hp": 5}
        direction = get_user_choice()
        expected = True
        actual = game.validate_move(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['w'])
    def test_validate_move_up_invalid(self, _):
        character = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        direction = get_user_choice()
        expected = False
        actual = game.validate_move(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['s'])
    def test_validate_move_down_invalid(self, _):
        character = {"x-coordinate": 0, "y-coordinate": 4, "current_hp": 5}
        direction = get_user_choice()
        expected = False
        actual = game.validate_move(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a'])
    def test_validate_move_left_invalid(self, _):
        character = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
        direction = get_user_choice()
        expected = False
        actual = game.validate_move(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['d'])
    def test_validate_move_right_invalid(self, _):
        character = {"x-coordinate": 4, "y-coordinate": 0, "current_hp": 5}
        direction = get_user_choice()
        expected = False
        actual = game.validate_move(character, direction)
        self.assertEqual(expected, actual)
