from unittest import TestCase

from game import evolve_final
import io
from unittest.mock import patch


class TestFinalEvolve(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_evolve(self, mock_stdout):
        test_monster = {'wins': 6, 'hp': 5, 'max_hp': 10,
                        'moves': {'flamethrower': {'power': 5, 'accuracy': 80}, 'slash': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        evolve_final(test_monster)
        expected = (
            "Wow! That is 6 wins for your monster! Your monster glows in a white light and begins to evolve\n"
            "Monster has reached final evolution! Stats and move power have maxed out. They have learned ['fire "
            "blast', 'crush']"
        )
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_evolve_fail(self, mock_stdout):
        test_monster = {'wins': 0, 'hp': 5, 'max_hp': 10,
                        'moves': {'flamethrower': {'power': 5, 'accuracy': 80}, 'slash': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        evolve_final(test_monster)
        expected = ''
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_evolve_3_wins(self, mock_stdout):
        test_monster = {'wins': 3, 'hp': 5, 'max_hp': 10,
                        'moves': {'flamethrower': {'power': 5, 'accuracy': 80}, 'slash': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        evolve_final(test_monster)
        expected = ''
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_evolve_more_than_6(self, mock_stdout):
        test_monster = {'wins': 8, 'hp': 5, 'max_hp': 10,
                        'moves': {'flamethrower': {'power': 5, 'accuracy': 80}, 'slash': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        evolve_final(test_monster)
        expected = (
            "Wow! That is 8 wins for your monster! Your monster glows in a white light and begins to evolve\n"
            "Monster has reached final evolution! Stats and move power have maxed out. They have learned ['fire "
            "blast', 'crush']"
        )
        self.assertEqual(mock_stdout.getvalue().strip(), expected)
