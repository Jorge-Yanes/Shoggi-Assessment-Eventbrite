from piece import *


class Cell:
    
    def __init__(self, column, row, piece):
        self._column = column
        self._row = row
        self._piece = Piece

    # returns the column where this cell is in the boar
    def get_column(self):
        return self._column

    # returns the row where this cell is in the boar
    def get_row(self):
        return self._row
    
    # returns the piece on this cell
    def get_piece(self):
        return self._piece

    # sets the piece on this cell
    def set_piece(self, piece):
        self._piece = piece


    column = property(get_column)
    row = property(get_row)
    piece = property(get_piece,set_piece)

