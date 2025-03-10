from unittest import TestCase
from unittest.mock import patch
import io
from battle import battle
from characters import make_monster, make_enemy


class TestBattle(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('random.randint', return_value=50)
    def test_battle_monster_wins(self, _, __, ___):
        name = 'nick'
        monster = make_monster(name)
        enemy = make_enemy()
        enemy['hp'] = 1
        actual = battle(monster, enemy)
        expected = "nick wins!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1'])
    @patch('random.randint', return_value=50)
    def test_battle_monster_lose(self, _, __, ___):
        name = 'nick'
        monster = make_monster(name)
        monster['hp'] = 1
        enemy = {'name': 'chris', 'hp': 50, 'max_hp': 100,
                 'moves': {'bite': {'power': 10, 'accuracy': 90}, 'punch': {'power': 10, 'accuracy': 100}}}
        actual = battle(monster, enemy)
        expected = "Enemy wins!"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '1', '1'])
    @patch('random.randint', return_value=50)
    def test_battle_monster_wins_multiple_turns(self, _, __, ___):
        name = 'nick'
        monster = make_monster(name)
        enemy = make_enemy()
        enemy['hp'] = 5
        actual = battle(monster, enemy)
        expected = "nick wins!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['1', '1'])
    @patch('random.randint', return_value=50)
    def test_battle_monster_lose_multi_turns(self, _, __, ___):
        name = 'nick'
        monster = make_monster(name)
        enemy = {'name': 'chris', 'hp': 50, 'max_hp': 100,
                 'moves': {'bite': {'power': 10, 'accuracy': 90}, 'punch': {'power': 10, 'accuracy': 100}}}
        actual = battle(monster, enemy)
        expected = (""
                    "Enemy wins!")
        self.assertEqual(expected, actual)
