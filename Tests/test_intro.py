from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from movement import intro


class TestIntro(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_intro(self, mock_stdout):
        expected = (
            "Thank you for trying my first game, this will be a battle simulation featuring your very own monster, "
            "your objective is, explore,\n"
            "get a total of 6 battle wins and defeat the final challenge, good luck! \n\n"
            "Well, it is finally time....Go set off on your adventure,\n"
            "but make sure to bring that crazy monster of "
            "yours for protection, umm... what was its name again?\n"
        )
        intro()
        actual = mock_stdout.getvalue()
        self.assertEqual(actual, expected)


