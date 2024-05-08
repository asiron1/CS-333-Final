import random

class Board:
    def __init__(self, gridSize, numBombs):
        self.gridSize = gridSize
        self.numBombs = numBombs

        self.board = self.make_new_board() 
        self.assign_values_to_board()

        self.dug = set() 

    def make_new_board(self):
        board = [[None for _ in range(self.gridSize)] for _ in range(self.gridSize)]

        i = 0
        while i < self.numBombs:
            loc = random.randint(0, self.gridSize**2 - 1) 
            row = loc // self.gridSize 
            col = loc % self.gridSize  

            if board[row][col] != '*':
                board[row][col] = '*' 
                i += 1

        return board
    
    def assign_values_to_board(self):
        for r in range(self.gridSize):
            for c in range(self.gridSize):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.gridSize-1, row+1)+1):
            for c in range(max(0, col-1), min(self.gridSize-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs
    
    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row-1), min(self.gridSize-1, row+1)+1):
            for c in range(max(0, col-1), min(self.gridSize-1, col+1)+1):
                if (r, c) in self.dug:
                    continue 
                self.dig(r, c)

        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.gridSize)] for _ in range(self.gridSize)]
        for row in range(self.gridSize):
            for col in range(self.gridSize):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        string_rep = ''
        widths = []
        for idx in range(self.gridSize):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        indices = [i for i in range(self.gridSize)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.gridSize)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep