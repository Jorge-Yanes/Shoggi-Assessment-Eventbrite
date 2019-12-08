from piece import *
from cell import *
from gold_general import *


class Pawn(Piece):

    def __init__(self, piece):

        self.player = piece.player
        self.piece_symbol = piece.piece_symbol
        self.crowned = piece.crowned

        Piece.set_piece_symbol("P")

    def move_is_possible(self, start, finish, piece, finish_piece):

        if start.row == finish.row and start.column == finish.column:
            return False

        if piece.crowned:
            # The crowned pawn has the same movements as the gold general
            return Gold_General.move_is_possible(self, start, finish, piece, finish_piece)

        # Depending to whom belongs the piece checks if the movement is allowed (one cell north)
        if piece.player == 1 and start.row - finish.row == -1 or piece.player == 2 and start.row - finish.row == 1:
            # If the movement is vertical
            if start.column == finish.column:
                # Checks if there is a piece in the end position and if its ours
                if finish_piece != None and piece.player == finish_piece.player:
                    return False
                return True
        return False
