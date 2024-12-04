from unittest import TestCase
from unittest.mock import patch
import movement


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=['w'])
    def test_get_user_choice_valid_input_valid(self, _):
        actual = movement.get_user_choice()
        expected = "w"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['s'])
    def test_get_user_choice_valid_new_input(self, _):
        actual = movement.get_user_choice()
        expected = "s"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a'])
    def test_get_user_choice_valid_a_input(self, _):
        actual = movement.get_user_choice()
        expected = "a"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['d'])
    def test_get_user_choice_valid_d_input(self, _):
        actual = movement.get_user_choice()
        expected = "d"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2', 'w'])
    def test_get_user_choice_valid_wrong_input(self, _):
        actual = movement.get_user_choice()
        expected = 'w'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2', 'hi', 'w'])
    def test_get_user_choice_valid_two_wrong_input(self, _):
        actual = movement.get_user_choice()
        expected = 'w'
        self.assertEqual(expected, actual)
