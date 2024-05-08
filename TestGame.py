import unittest
from unittest.mock import patch
from game import play_game

class TestGame(unittest.TestCase):
    def test_play_game(self):
        # Define a mock input sequence
        mock_inputs = [
            '1,1',   # First input to select a cell
            '0,0',   # Continue playing
            '2,2',   # Next input
            '9,9',   # Continue playing
            '3,3',   # Next input
            'no'     # End the game
        ]

        # Patch the input function with the mock inputs
        with patch('builtins.input', side_effect=mock_inputs):
            play_game()

if __name__ == '__main__':
    unittest.main()
