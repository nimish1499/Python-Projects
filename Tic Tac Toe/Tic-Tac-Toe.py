import os

os.system("cls")


class Board:

    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print((self.cells[1] + '|' + self.cells[2] + '|' + self.cells[3]))
        print('-+-+-')
        print((self.cells[4] + '|' + self.cells[5] + '|' + self.cells[6]))
        print('-+-+-')
        print((self.cells[7] + '|' + self.cells[8] + '|' + self.cells[9]))

    def update_board(self, cell_pos, chance):
        if self.cells[cell_pos] == " ":
            self.cells[cell_pos] = chance

    def is_winner(self, chance):
        for win_combination in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
            result = True
            for cell_no in win_combination:
                if self.cells[cell_no] != chance:
                    result = False

            if result:
                return True

        return False

    def is_tie(self):
        used_cell = 0
        for i in self.cells:
            if i != " ":
                used_cell += 1
        if used_cell == 9:
            return True
        else:
            return False

    def reset(self):
        self.cells = []
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


board = Board()


def print_header():
    print('Welcome to Tic-Tac-Toe\n')


def refresh_screen():
    # Clear the screen
    os.system("cls")

    print_header()
    # Showing board
    board.display()


refresh_screen()

while True:
    X_input = int(input('X_chance: Choose between 1-9 > '))
    # Board Update
    board.update_board(X_input, 'X')
    refresh_screen()

    # Check for X win
    if board.is_winner('X'):
        print('\nX Wins!\n')
        play_again = input("Would you Like to Play Again? [Y/N]").upper()
        if play_again == 'Y':
            continue
        else:
            break

    # Check for Tie
    if board.is_tie():
        print('\nTie Game!\n')
        play_again = input("Would you Like to Play Again? [Y/N]").upper()
        if play_again == 'Y':
            continue
        else:
            break

    O_input = int(input('0_chance: Choose between 1-9 > '))
    # Board Update
    board.update_board(O_input, 'O')
    board.is_winner('O')
    refresh_screen()

    # Check for O win
    if board.is_winner('O'):
        print('\nO Wins!\n')
        play_again = input("Would you Like to Play Again? [Y/N]")
        if play_again == 'Y':
            board.reset()
        else:
            break

    # Check for Tie
    if board.is_tie():
        print('\nTie Game!\n')
        play_again = input("Would you Like to Play Again? [Y/N]").upper()
        if play_again == 'Y':
            continue
        else:
            break
