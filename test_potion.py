import io
from unittest import TestCase
from unittest.mock import patch

from game import potion


class TestPotion(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_potion_with_uses_left(self, mock_stdout):
        test_monster = {'name': 'nick', 'wins': 0, 'hp': 1, 'max_hp': 10,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        potion(test_monster)
        expected_output = "Potion used! nicks HP restored to max. Potions left: 1"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_potion_with_1_use_left(self, mock_stdout):
        test_monster = {'name': 'nick','wins': 0, 'hp': 2, 'max_hp': 10,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 1}
        potion(test_monster)
        expected_output = "Potion used! nicks HP restored to max. Potions left: 0"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_potion_with_0_use_left(self, mock_stdout):
        test_monster = {'name': 'nick', 'wins': 0, 'hp': 2, 'max_hp': 10,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 0}
        potion(test_monster)
        expected_output = "No potions left to use!"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
