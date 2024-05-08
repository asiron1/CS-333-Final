from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from minesweeper import play_game

class TestMinesweeperIntegration(TestCase):
    def setUp(self):
        self.mock_stdout = StringIO()

    def tearDown(self):
        print(self.mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_game_win(self, mock_input, mock_stdout):
        mock_input.side_effect = ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2', 'no']
        play_game(gridSize=3, numBombs=0)
        output = mock_stdout.getvalue()
        self.assertIn("You Win!", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_game_loss(self, mock_input, mock_stdout):
        mock_input.side_effect = ['0,0', 'no']
        play_game(gridSize=3, numBombs=9)
        output = mock_stdout.getvalue()
        self.assertIn("Thanks for playing!", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_invalid_input(self, mock_input, mock_stdout):
        mock_input.side_effect = ['invalid', '0,0', '0,1', 'no']
        play_game(gridSize=3, numBombs=3)
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please provide row and column numbers separated by a comma.", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_play_again_yes(self, mock_input, mock_stdout):
        mock_input.side_effect = ['0,0', 'yes', '0,0', 'no']
        play_game(gridSize=3, numBombs=0)
        output = mock_stdout.getvalue()
        self.assertIn("You Win!", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_play_again_no(self, mock_input, mock_stdout):
        mock_input.side_effect = ['0,0', 'no']
        play_game(gridSize=3, numBombs=0)
        output = mock_stdout.getvalue()
        self.assertIn("Thanks for playing!", output)
