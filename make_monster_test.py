from unittest import TestCase
from game import make_monster


class Test(TestCase):
    def test_make_monster_x(self):
        monster = make_monster()
        self.assertIn("x-coordinate", monster.keys())

    def test_make_monster_y(self):
        monster = make_monster()
        self.assertIn("y-coordinate", monster.keys())

    def test_make_monster_wins(self):
        monster = make_monster()
        self.assertIn("wins", monster.keys())

    def test_make_monster_moves(self):
        monster = make_monster()
        self.assertIn("moves", monster.keys())

    def test_make_monster_potions(self):
        monster = make_monster()
        self.assertIn("potion_uses", monster.keys())
