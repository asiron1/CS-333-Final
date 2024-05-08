from board import Board
from player import Player

def play_game(gridSize=10, numBombs=10):
    print("demo video")
    while True:
        board = Board(gridSize, numBombs)
        player = Player()

        safe = True

        while len(board.dug) < board.gridSize ** 2 - numBombs:
            print(board)
            row, col = player.get_input()
            if row < 0 or row >= board.gridSize or col < 0 or col >= gridSize:
                print("Invalid location. Try again.")
                continue

            safe = board.dig(row, col)
            if not safe:
                break

        if safe:
            print("You Win!")
        else:
            print("Game Over")
            board.dug = {(r,c) for r in range(board.gridSize) for c in range(board.gridSize)}

        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again in {"yes", "no"}:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again != "yes":
            print("Thanks for playing!")
            break
