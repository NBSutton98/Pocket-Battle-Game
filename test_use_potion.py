from unittest import TestCase
from game import use_potion
import io
from unittest.mock import patch


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])  # Mocking input to simulate user entering '1'
    def test_use_potion(self, mock_input, mock_stdout):
        test_monster = {'hp': 1, 'max_hp': 10, 'potion_uses': 3}
        use_potion(test_monster)
        expected = "Potion used! Monster's HP restored to max. Potions left: 2"
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

