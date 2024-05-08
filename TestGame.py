import unittest
from unittest.mock import patch
from game import play_game

class TestGame(unittest.TestCase):
    def test_play_game(self):
        # Since the game is random i cant predict where the bombs are. so the test only works if it hits a bomb
        mock_inputs = [
            '1,1',   
            '0,0',   
            '2,2',   
            '9,9',   
            '4,4',  
            '3,3', 
            '5,5', 
            '6,6', 
            '7,7', 
            '8,8', 
            'no'     
        ]

        with patch('builtins.input', side_effect=mock_inputs):
            play_game()

if __name__ == '__main__':
    unittest.main()
