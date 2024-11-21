from unittest import TestCase
from unittest.mock import patch
from game import make_monster, make_enemy, use_move


class TestUseMove(TestCase):
    @patch('random.randint', return_value=50)
    def test_use_move(self, _):
        monster = make_monster()
        enemy = make_enemy()
        move = 'ember'
        damage = 5
        enemy['hp'] -= damage
        use_move(monster, enemy, move)
        self.assertEqual(enemy['hp'], 0)
