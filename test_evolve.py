from unittest import TestCase
from game import make_enemy
from game import evolve

class Test(TestCase):

    def test_evolve(self):
        monster = {'wins': 3, 'hp': 5, 'max_hp': 10,
                   'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
                   'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
        enemy = make_enemy()
        actual = evolve(monster, enemy)
        expected = {'wins': 3, 'hp': 5, 'max_hp': 10,   }
        self.assertEqual(actual, expected)
