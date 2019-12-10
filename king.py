from piece import *

class King(Piece):
    piece_symbol = 'K'

    def __init__(self, piece):

        self.player = piece.player
        self.piece_symbol = piece.piece_symbol
        self.crowned = False

    def move_is_possible(self, start, finish, piece, finish_piece):
        # Checks if there is movement
        if start.row == finish.row and start.column == finish.column:
            return False
        # Checks if there is a piece in the end position and if its ours
        if finish_piece != None and piece.player == finish_piece.player:
            return False
        # Allows all one cell movements
        if abs(start.row - finish.row) <= 1 and abs(start.column - finish.column) <= 1:
            return True
        return False
