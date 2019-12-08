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

'''

    public boolean canMove(Square from, Square to, Board b) {
		if((Math.abs(from.getR() - to.getR()) <= 1 && 
				(Math.abs(from.getC() - to.getC()) <= 1))) {
			if(owner == 1) {
				//If Piece is moving backwards check for diagonal
				if(from.getR() - to.getR() == 1) {
					if(from.getC() != to.getC()) {
						return false;
					}
				}
			} else if(owner == 2) {
				//If Piece is moving backwards check for diagonal
				if(from.getR() - to.getR() == -1) {
					if(from.getC() != to.getC()) {
						return false;
					}
				}
			}
			if(to.getPiece() != null) {
				if(from.getPiece().getOwner() == to.getPiece().getOwner()) {
					return false;
				}
			}
			return true;
		}
		return false;
	}
    
    
    
    '''