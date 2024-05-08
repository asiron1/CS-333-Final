import unittest
from unittest.mock import patch
from board import Board

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

if __name__ == '__main__':
    unittest.main()