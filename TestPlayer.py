import unittest
from unittest.mock import patch
from player import Player

class TestPlayer(unittest.TestCase):
    @patch('builtins.input', side_effect=['1,2'])
    def test_get_input_valid(self, mock_input):
        player = Player()
        row, col = player.get_input()
        self.assertEqual(row, 1)
        self.assertEqual(col, 2)

    @patch('builtins.input', side_effect=['invalid', '1,2'])
    def test_get_input_invalid_then_valid(self, mock_input):
        player = Player()
        row, col = player.get_input()
        self.assertEqual(row, 1)
        self.assertEqual(col, 2)

if __name__ == '__main__':
    unittest.main()
