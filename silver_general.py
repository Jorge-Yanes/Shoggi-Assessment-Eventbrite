from piece import *
from cell import *
from gold_general import *


class Silver_General(Piece):
    piece_symbol = 'S'

    def __init__(self, piece):

        self.player = piece.player
        self.piece_symbol = piece.piece_symbol
        self.crowned = piece.crowned

    def move_is_possible(self, start, finish, piece, finish_piece):
        if start.row == finish.row and start.column == finish.column:
            return False

        if piece.crowned:
            # The crowned silver general has the same movements as the gold general
            return Gold_General.move_is_possible(self, start, finish, piece, finish_piece)

        if abs(start.row - finish.row) <= 1 and abs(start.column - finish.column) <= 1:
            # Allow diagonal backward movement, for player 1
            if piece.player == 1 and start.row-finish.row == 1 and start.column == finish.column:
                return False
            # Allow diagonal backward movement, for player 2
            elif piece.player == 2 and start.row-finish.row == -1 and start.column == finish.column:
                return False
            # Checks if there is a piece in the end position and if its ours
            if finish_piece != None and piece.player == finish_piece.player:
                return False
            # Not allow sideways movements
            if start.row == finish.row:
                return False
            return True
        return False
