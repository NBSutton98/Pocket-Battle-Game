from unittest import TestCase
from game import make_enemy

class TestMakeEnemy(TestCase):
    def test_enemy_hp(self):
        enemy = make_enemy()
        self.assertIn("hp", enemy.keys())

    def test_enemy_max_hp(self):
        enemy = make_enemy()
        self.assertIn("max_hp", enemy.keys())

    def test_enemy_moves(self):
        enemy = make_enemy()
        self.assertIn("moves", enemy.keys())

    def test_enemy_bite(self):
        enemy = make_enemy()
        self.assertIn("bite", enemy['moves'].keys())

    def test_enemy_bite_power(self):
        enemy = make_enemy()
        self.assertIn("power", enemy['moves']['bite'].keys())

