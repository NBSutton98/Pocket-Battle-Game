from unittest import TestCase
from unittest.mock import patch
from characters import make_monster
from movement import get_user_choice, move_monster



class Test(TestCase):

    @patch('builtins.input', side_effect=['s'])
    def test_move_character_up(self, _):
        name = 'nick'
        character = make_monster(name)
        direction = get_user_choice()
        expected = True
        actual = move_monster(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['w'])
    def test_move_character_down(self, _):
        name = 'nick'
        character = make_monster(name)
        direction = get_user_choice()
        expected = True
        actual = move_monster(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['d'])
    def test_move_character_right(self, _):
        name = 'nick'
        character = make_monster(name)
        direction = get_user_choice()
        expected = True
        actual = move_monster(character, direction)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a'])
    def test_move_character_left(self, _):
        name = 'nick'
        character = make_monster(name)
        direction = get_user_choice()
        expected = True
        actual = move_monster(character, direction)
        self.assertEqual(expected, actual)
