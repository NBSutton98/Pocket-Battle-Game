from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from movement import text_delay


class TestTextDelay(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    @patch('time.sleep', return_value=None)
    def test_text_delay_words(self, mock_sleep, mock_stdout):
        expected = "hello"
        text_delay("hello")
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
        self.assertEqual(mock_sleep.call_count, len("hello"))

    @patch('sys.stdout', new_callable=StringIO)
    @patch('time.sleep', return_value=None)
    def test_text_delay_numbers(self, mock_sleep, mock_stdout):
        expected = "5"
        text_delay("5")
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
        self.assertEqual(mock_sleep.call_count, len("5"))

    @patch('sys.stdout', new_callable=StringIO)
    @patch('time.sleep', return_value=None)
    def test_text_delay_multi_words(self, mock_sleep, mock_stdout):
        expected = "hello and goodbye"
        text_delay("hello and goodbye")
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)
        self.assertEqual(mock_sleep.call_count, len("hello and goodbye"))
