import unittest
from unittest.mock import patch
from io import StringIO
from board import Board
from game import play_game
from minesweeper import play_game as minesweeper_play_game
from player import Player

class TestBoard(unittest.TestCase):
    def test_board_creation(self):
        # Test if the board is created with the correct size and number of bombs
        board = Board(gridSize=10, numBombs=10)
        self.assertEqual(board.gridSize, 10)
        self.assertEqual(len(board.dug), 0)  # No cells dug initially

    def test_board_digging(self):
        # Mocking the random number generator to place bombs at a specific location
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 0  # Placing a bomb at location (0, 0)
            
            # Test if digging works as expected
            board = Board(gridSize=3, numBombs=1)
            
            # Digging at a cell without a bomb
            row, col = 1, 1
            dug_before = len(board.dug)
            safe = board.dig(row, col)
            self.assertTrue(safe)  # Digging should be safe as no bomb is present at (1, 1)
            self.assertEqual(len(board.dug), dug_before + 1)  # One cell should be dug
            
            # Digging at a cell with a bomb
            row, col = 0, 0
            dug_before = len(board.dug)
            safe = board.dig(row, col)
            self.assertFalse(safe)  # Digging at a bomb should not be safe
            self.assertEqual(len(board.dug), dug_before + 1)  # Only one cell should be dug even if it's a bomb

    def test_board_bomb_distribution(self):
        # Test if the correct number of bombs are distributed on the board
        gridSize = 10
        numBombs = 10
        board = Board(gridSize=gridSize, numBombs=numBombs)
        bomb_count = sum(row.count('*') for row in board.board)
        self.assertEqual(bomb_count, numBombs)

    def test_board_neighbors(self):
        # Test if the number of neighboring bombs is correct for non-bomb cells
        gridSize = 5
        numBombs = 5
        board = Board(gridSize=gridSize, numBombs=numBombs)
        for r in range(gridSize):
            for c in range(gridSize):
                if board.board[r][c] != '*':
                    neighbors = board.get_num_neighboring_bombs(r, c)
                    self.assertGreaterEqual(neighbors, 0)
                    self.assertLessEqual(neighbors, 8)  # Max neighbors for any cell is 8

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

class TestMinesweeperIntegration(unittest.TestCase):
    def setUp(self):
        self.mock_stdout = StringIO()

    def tearDown(self):
        print(self.mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_game_win(self, mock_input, mock_stdout):
        mock_input.side_effect = ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2', 'no']
        minesweeper_play_game(gridSize=3, numBombs=0)
        output = mock_stdout.getvalue()
        self.assertIn("You Win!", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_game_loss(self, mock_input, mock_stdout):
        mock_input.side_effect = ['0,0', 'no']
        minesweeper_play_game(gridSize=3, numBombs=9)
        output = mock_stdout.getvalue()
        self.assertIn("Thanks for playing!", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_invalid_input(self, mock_input, mock_stdout):
        mock_input.side_effect = ['invalid', '0,0', '0,1', 'no']
        minesweeper_play_game(gridSize=3, numBombs=3)
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please provide row and column numbers separated by a comma.", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_play_again_yes(self, mock_input, mock_stdout):
        mock_input.side_effect = ['0,0', 'yes', '0,0', 'no']
        minesweeper_play_game(gridSize=3, numBombs=0)
        output = mock_stdout.getvalue()
        self.assertIn("You Win!", output)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input')
    def test_play_again_no(self, mock_input, mock_stdout):
        mock_input.side_effect = ['0,0', 'no']
        minesweeper_play_game(gridSize=3, numBombs=0)
        output = mock_stdout.getvalue()
        self.assertIn("Thanks for playing!", output)

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
