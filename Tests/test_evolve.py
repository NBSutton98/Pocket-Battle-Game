import io
from unittest import TestCase
from unittest.mock import patch

from characters import make_enemy
from evolve import evolve


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evolve(self, mock_stdout):
        test_monster = {'name': 'nick', 'wins': 3, 'hp': 5, 'max_hp': 10,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        test_enemy = make_enemy()
        evolve(test_monster, test_enemy)

        expected = ("Wow! That is 3 wins for your monster! Your monster glows in a white light and begins to evolve\n"
                    "nick evolved! Stats increased. They have learned ['flamethrower', 'slash']\n"
                    "Your enemy has evolved into, Balloonist")

        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evolve_fail(self, mock_stdout):
        test_monster = {'name': 'nick', 'wins': 0, 'hp': 5, 'max_hp': 10,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        test_enemy = make_enemy()
        evolve(test_monster, test_enemy)
        expected = ''
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evolve_fail_1_win(self, mock_stdout):
        test_monster = {'name': 'nick', 'wins': 1, 'hp': 5, 'max_hp': 10,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        test_enemy = make_enemy()
        evolve(test_monster, test_enemy)
        expected = ''
        self.assertEqual(mock_stdout.getvalue().strip(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evolve_fail_2_win(self, mock_stdout):
        test_monster = {'name': 'nick', 'wins': 2, 'hp': 5, 'max_hp': 10,
                        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                        'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        test_enemy = make_enemy()
        evolve(test_monster, test_enemy)
        expected = ''
        self.assertEqual(mock_stdout.getvalue().strip(), expected)
