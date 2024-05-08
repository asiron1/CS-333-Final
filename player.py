import re

class Player:
    def get_input(self):
        while True:
            try:
                user_input = input("Where would you like to dig? Input as row,col: ")
                row, col = map(int, user_input.split(','))
                return row, col
            except ValueError:
                print("Invalid input. Please provide row and column numbers separated by a comma.")
