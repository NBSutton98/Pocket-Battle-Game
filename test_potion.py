from unittest import TestCase
from game import potion
import io
from unittest.mock import patch

class TestPotion(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_potion_with_uses_left(self, mock_stdout):
        test_monster = {
            'wins': 0,
            'hp': 1,
            'max_hp': 10,
            'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
            'x-coordinate': 0,
            'y-coordinate': 0,
            'potion_uses': 2
        }
        potion(test_monster)
        expected_output = "Potion used! Monster's HP restored to max. Potions left: 1"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
