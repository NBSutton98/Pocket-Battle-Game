from unittest import TestCase
from unittest.mock import patch
import io
from battle import final_battle
from characters import make_monster, make_enemy


class TestBattle(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('random.randint', return_value=50)
    def test_final_battle_win(self, _, __, ___):
        name = 'nick'
        monster = make_monster(name)
        enemy = make_enemy()
        enemy['hp'] = 1
        actual = final_battle(monster, enemy)
        expected = True
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('random.randint', return_value=50)
    def test_final_battle_lose(self, _, __, ___):
        name = 'nick'
        monster = make_monster(name)
        monster['hp'] = 1
        enemy = make_enemy()
        actual = final_battle(monster, enemy)
        expected = False
        self.assertEqual(expected, actual)
