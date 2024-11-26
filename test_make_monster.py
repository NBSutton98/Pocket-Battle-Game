from unittest import TestCase
from characters import make_monster


class Test(TestCase):
    def test_make_monster_x(self):
        name = 'chris'
        monster = make_monster(name)
        self.assertIn("x-coordinate", monster.keys())

    def test_make_monster_y(self):
        name = 'chris'
        monster = make_monster(name)
        self.assertIn("y-coordinate", monster.keys())

    def test_make_monster_wins(self):
        name = 'chris'
        monster = make_monster(name)
        self.assertIn("wins", monster.keys())

    def test_make_monster_moves(self):
        name = 'chris'
        monster = make_monster(name)
        self.assertIn("moves", monster.keys())

    def test_make_monster_potions(self):
        name = 'chris'
        monster = make_monster(name)
        self.assertIn("potion_uses", monster.keys())

    def test_make_monster_ember(self):
        name = 'chris'
        monster = make_monster(name)
        self.assertIn("ember", monster['moves'].keys())

    def test_make_monster_power(self):
        name = 'chris'
        monster = make_monster(name)
        self.assertIn("power", monster['moves']['ember'].keys())
