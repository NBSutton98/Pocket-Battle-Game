from unittest import TestCase
from battle import move_choice
import io
from unittest.mock import patch


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_move_choice(self, _, __):
        test_monster = {'wins': 0, 'hp': 5, 'max_hp': 10,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        actual = move_choice(test_monster)
        expected = 'ember'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2'])
    def test_move_choice_2(self, _, __):
        test_monster = {'wins': 0, 'hp': 5, 'max_hp': 1,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        actual = move_choice(test_monster)
        expected = 'scratch'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3', '2'])
    def test_move_choice_invalid_number(self, _, __):
        test_monster = {'wins': 0, 'hp': 5, 'max_hp': 3,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        actual = move_choice(test_monster)
        expected = 'scratch'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['w', '2'])
    def test_move_choice_invalid_letter(self, _, __):
        test_monster = {'wins': 0, 'hp': 5, 'max_hp': 5,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        actual = move_choice(test_monster)
        expected = 'scratch'
        self.assertEqual(expected, actual)
