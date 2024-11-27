from unittest import TestCase
from healing import use_potion
import io
from unittest.mock import patch


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_use_potion(self, _, mock_stdout):
        test_monster = {'name': 'chris', 'hp': 1, 'max_hp': 10, 'potion_uses': 3}
        use_potion(test_monster)
        expected = "Potion used!\n chriss HP restored to max. Potions left: 2"
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    def test_use_potion_last(self, _, mock_stdout):
        test_monster = {'name': 'chris', 'hp': 1, 'max_hp': 10, 'potion_uses': 1}
        use_potion(test_monster)
        expected = "Potion used!\n chriss HP restored to max. Potions left: 0"
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2'])
    def test_use_potion_decline(self, _, mock_stdout):
        test_monster = {'name': 'chris', 'hp': 1, 'max_hp': 10, 'potion_uses': 1}
        use_potion(test_monster)
        expected = "Continuing without healing."
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['w', '1'])
    def test_use_potion_invalid(self, _, mock_stdout):
        test_monster = {'name': 'chris', 'hp': 1, 'max_hp': 10, 'potion_uses': 1}
        use_potion(test_monster)
        expected = (
            "Invalid choice! Please enter '1' or '2'."
            "Potion used!\n chriss HP restored to max. Potions left: 0"
        )
        self.assertEqual(mock_stdout.getvalue().strip(), expected)
