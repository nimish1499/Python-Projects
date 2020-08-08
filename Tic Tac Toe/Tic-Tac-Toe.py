from os import system
# os.system("cls")


def clear():
    system('cls')


class Board:
    def __init__(self):
        self.cells = ["", "", "", "", "", "", "", "", "", ""]

    def display(self):
        print("%s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print('---------')
        print("%s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print('---------')
        print("%s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))


board = Board()


def print_header():
    print('Welcome to Tic-Tac-Toe\n')


def refresh_screen():
    # Clear the screen
    # os.system("cls")
    clear()

    # Print header
    print_header()
    # Showing board
    board.display()


# while True:
refresh_screen()


