from piece import *
from cell import *


class Gold_General(Piece):
    piece_symbol = 'G'

    def __init__(self, piece):

        self.player = piece.player
        self.piece_symbol = piece.piece_symbol
        self.crowned = piece.crowned

        Piece.set_piece_symbol("G")

    def move_is_possible(self, start, finish, piece, finish_piece):
        if start.row == finish.row and start.column == finish.column:
            return False
        if abs(start.row - finish.row) <= 1 and abs(start.column - finish.column) <= 1:
            # Allow backward movement, except for the diagonal, for player 1
            if piece.player == 1 and start.row-finish.row == 1 and start.column != finish.column:
                return False
            # Allow backward movement, except for the diagonal, for player 2
            elif piece.player == 2 and start.row-finish.row == -1 and start.column != finish.column:
                return False
            # Checks if there is a piece in the end position and if its ours
            if finish_piece != None and piece.player == finish_piece.player:
                return False
            return True
        return False
