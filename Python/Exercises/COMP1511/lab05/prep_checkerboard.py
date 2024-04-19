BOARD_LENGTH = 8
PIECE_RED = 'R'
PIECE_BLACK = 'B'
PIECE_EMPTY = ' '
TYPE_KING = 1
TYPE_NORMAL = 0 

class BoardSquare():
    def __init__(self, isKing, piece_colour):
        self.isKing = isKing
        self.piece_colour = piece_colour


def print_checkerboard(board):
    for row in range(BOARD_LENGTH):
        print("+-----+-----+-----+-----+-----+-----+-----+-----+")
        print("|", end = "")
        for col in range(BOARD_LENGTH):
            if (board[row][col].isKing == TYPE_KING):
                print(" " + board[row][col].piece_colour + "-K |", end = "")
            else:
                print("  " + board[row][col].piece_colour + "  |", end = "")
        print()
    print("+-----+-----+-----+-----+-----+-----+-----+-----+")

def read_input():
    print("Please enter pieces: ")
    pieces = [[BoardSquare(TYPE_NORMAL, PIECE_EMPTY) for i in range(BOARD_LENGTH)] for j in range(BOARD_LENGTH)]

    while True:
        try:
            row, col, colour, isKing = input().split()
            pieces[int(row)][int(col)] = BoardSquare(int(isKing), colour)
        except EOFError:
            break
    
    print_checkerboard(pieces)

read_input()
