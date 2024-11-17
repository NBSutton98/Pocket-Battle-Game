from unittest import TestCase
from game import potion
from game import make_monster


class Test(TestCase):
    def test_potion(self):
        monster = make_monster()
        actual = potion(monster)
        expected = "Potion used! Monster's HP restored to max. Potions left: 2"
        self.assertEqual(actual, expected)
