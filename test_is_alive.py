from unittest import TestCase

from game import is_alive
from game import make_monster


class Test(TestCase):
    def test_is_alive(self):
        name = 'chris'
        monster = make_monster(name)
        actual = is_alive(monster)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_false(self):
        name = 'chris'
        monster = make_monster(name)
        monster['hp'] = 0
        actual = is_alive(monster)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_alive_weak(self):
        name = 'chris'
        monster = make_monster(name)
        monster['hp'] = 1
        actual = is_alive(monster)
        expected = True
        self.assertEqual(actual, expected)
