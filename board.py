from cell import *
from pawn import *
from gold_general import *
from silver_general import *
from king import *


class Board(object):

    board = [[Cell(c, r) for c in range(9)] for r in range(9)]

    for p in range(9):
        board[2][p] = Pawn
        board[2][p].player = 1
        board[6][p] = Pawn
        board[6][p].player = 2

    board[0][3] = Gold_General
    board[0][3].player = 1
    board[0][5] = Gold_General
    board[0][5].player = 1
    board[8][3] = Gold_General
    board[8][3].player = 2
    board[8][5] = Gold_General
    board[8][5].player = 2
    board[0][2] = Silver_General
    board[0][2].player = 1
    board[0][6] = Silver_General
    board[0][6].player = 1
    board[8][2] = Silver_General
    board[8][2].player = 2
    board[8][6] = Silver_General
    board[8][6].player = 2
    board[0][4] = King
    board[0][4].player = 1
    board[8][4] = King 
    board[8][4].player = 2
    

    def get_cell(self, r, c):
        return self.board[r][c]
    a = 0
    z = '    '
    for b in range(9):
        z += str(b)+'  '
    print(z)
    print("  +----------------------------+")

    for x in board:
        s = str(a)+' | '
        for y in x:
            if hasattr(y, 'piece_symbol'):
                s += str(y.piece_symbol)+'  '
            else:
                s += '  '+' '
        print(s + '|')
        a += 1
    print("  +----------------------------+")
