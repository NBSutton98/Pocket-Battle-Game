from unittest import TestCase
from game import use_potion
from game import potion
from unittest.mock import patch

class Test(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_use_potion(self, _):
        test_monster = {'hp': 1, 'max_hp': 10, 'potion_uses': 3}
        actual = use_potion(test_monster)
        expected = "Monster wins!"
        self.assertEqual(actual, expected)
