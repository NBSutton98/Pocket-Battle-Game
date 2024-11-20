from unittest import TestCase
from game import battle, make_monster, make_enemy
import io
from unittest.mock import patch


class TestBattle(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('random.randint', return_value=50)
    def test_battle_monster_wins(self, mock_stdout, mock_input, mock_randint):
        monster = make_monster()
        enemy = make_enemy()
        actual = battle(monster, enemy)
        expected = "Monster wins!"
        self.assertEqual(expected, actual)

