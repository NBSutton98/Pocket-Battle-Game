from unittest import TestCase
from unittest.mock import patch
import io
from game import battle, make_monster, make_enemy


class TestBattle(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('random.randint', return_value=50)
    def test_battle_monster_wins(self, mock_stdout, mock_input, mock_randint):
        monster = make_monster()
        enemy = make_enemy()
        enemy['hp'] = 1
        actual = battle(monster, enemy)
        expected = "Monster wins!"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    @patch('random.randint', return_value=50)
    def test_battle_monster_lose(self, mock_stdout, mock_input, mock_randint):
        monster = make_monster()
        monster['hp'] = 1
        enemy = {'hp': 100, 'max_hp': 100,
                 'moves': {'bite': {'power': 10, 'accuracy': 90}, 'punch': {'power': 10, 'accuracy': 100}}}
        actual = battle(monster, enemy)
        expected = "Enemy wins!"
        self.assertEqual(expected, actual)
