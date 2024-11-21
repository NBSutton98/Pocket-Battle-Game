from unittest import TestCase
from game import make_monster
from game import is_alive


class Test(TestCase):
    def test_is_alive(self):
        monster = make_monster()
        actual = is_alive(monster)
        expected = True
        self.assertEqual(actual, expected)
