from unittest import TestCase
from game import make_final_boss

class Test(TestCase):
    def test_make_final_hp(self):
        final_boss = make_final_boss()
        self.assertIn("hp", final_boss.keys())

    def test_make_final_max(self):
        final_boss = make_final_boss()
        self.assertIn("max_hp", final_boss.keys())

    def test_make_final_moves(self):
        final_boss = make_final_boss()
        self.assertIn("moves", final_boss.keys())

    def test_make_final_punch(self):
        final_boss = make_final_boss()
        self.assertIn("big punch", final_boss['moves'].keys())

    def test_make_final_POWER(self):
        final_boss = make_final_boss()
        self.assertIn("power", final_boss['moves']['big punch'].keys())