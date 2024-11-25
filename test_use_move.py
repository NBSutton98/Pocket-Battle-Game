from unittest import TestCase
from unittest.mock import patch
from game import make_monster, make_enemy, use_move


class TestUseMove(TestCase):
    @patch('random.randint', return_value=50)
    def test_use_move_death(self, _):
        name = 'chris'
        monster = make_monster(name)
        enemy = make_enemy()
        move = 'ember'
        damage = 5
        enemy['hp'] -= damage
        use_move(monster, enemy, move)
        self.assertEqual(enemy['hp'], 0)

    @patch('random.randint', return_value=50)
    def test_use_move_2_death(self, _):
        name = 'chris'
        monster = make_monster(name)
        enemy = make_enemy()
        move = 'scratch'
        damage = 5
        enemy['hp'] -= damage
        use_move(monster, enemy, move)
        self.assertEqual(enemy['hp'], 0)

    @patch('random.randint', return_value=50)
    def test_use_move_alive(self, _):
        name = 'chris'
        monster = make_monster(name)
        enemy = make_enemy()
        move = 'scratch'
        damage = 1
        enemy['hp'] -= damage
        use_move(monster, enemy, move)
        self.assertEqual(enemy['hp'], 2)

    @patch('random.randint', return_value=50)
    def test_use_move_alive_second_move(self, _):
        name = 'chris'
        monster = make_monster(name)
        enemy = make_enemy()
        move = 'ember'
        damage = 1
        enemy['hp'] -= damage
        use_move(monster, enemy, move)
        self.assertEqual(enemy['hp'], 1)

