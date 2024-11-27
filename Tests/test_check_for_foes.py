from unittest import TestCase
from unittest.mock import patch
import movement


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_check_for_foes_foe_found(self, _):
        actual = movement.check_for_foes()
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_check_for_foes_foe_not_found(self, _):
        actual = movement.check_for_foes()
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)
    def test_check_for_foes_min(self, _):
        actual = movement.check_for_foes()
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=4)
    def test_check_for_foes_max(self, _):
        actual = movement.check_for_foes()
        expected = False
        self.assertEqual(actual, expected)