import unittest
from pawn import *
from random import randint
from pawn import Pawn
from cell import Cell


class TestClass(unittest.TestCase):

    # Test cases with allowed moves
    def test_move_is_possible(self):

        for a in range(8):
            # Piece that we are going to move
            piece_1 = Piece(player=1, piece_symbol='P', crowned=False)
           
            # Possible piece at the final position
            finish_piece = None

            # Starting and finishing positions
            start_cell_1 = Cell(column=a, row=a, piece=piece_1)
            finish_cell_1 = Cell(column=a, row=a+1, piece=finish_piece)

            # Allowed movement where the final cell is empty
            self.assertTrue(Pawn.move_is_possible(None, start_cell_1, finish_cell_1, piece_1, finish_piece))
       
            # Allowed movement where the final cell is occupied by an opponents piece
            self.assertTrue(Pawn.move_is_possible(None, start_cell_1, finish_cell_1, piece_1, finish_piece=Piece(player=2, piece_symbol='P', crowned=False)))

            # Allowed movement with different player and starting and finishing cells 
            piece_2 = Piece(player=2, piece_symbol='P',crowned=False)
            start_cell_2 = Cell(column=a, row=a+1, piece=piece_2)
            finish_cell_2 = Cell(column=a, row=a, piece=finish_piece)
            
            # Allowed movement where the final cell is empty
            self.assertTrue(Pawn.move_is_possible(None, start_cell_2, finish_cell_2, piece_2, finish_piece))
       
            # Allowed movement where the final cell is occupied by an opponents piece
            self.assertTrue(Pawn.move_is_possible(None, start_cell_2, finish_cell_2, piece_2, finish_piece=Piece(player=1, piece_symbol='P', crowned=False)))

            #Starting and finishing cells are the same
            self.assertFalse(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a, row=a, piece=finish_piece), piece_1, finish_piece))

    def test_move_is_possible_crowned(self):
        for a in range(8):
            # Crowned piece that we are going to move
            piece_1 = Piece(player=1, piece_symbol='P', crowned=True)

            # Piece at the final position
            finish_piece = None

            # One cell fordward, allowed movement where the final cell is empty
            self.assertTrue(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a, row=a+1, piece=finish_piece), piece_1, finish_piece))

            # One cell backward, allowed movement where the final cell is empty
            self.assertTrue(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a, row=a-1, piece=finish_piece), piece_1, finish_piece))
 
            # One cell to the right, allowed movement where the final cell is empty
            self.assertTrue(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a+1, row=a, piece=finish_piece), piece_1, finish_piece))
            
            # One cell to the left, allowed movement where the final cell is empty
            self.assertTrue(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a-1, row=a, piece=finish_piece), piece_1, finish_piece))

            # Top-right diagonal, allowed movement where the final cell is empty
            self.assertTrue(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a+1, row=a+1, piece=finish_piece), piece_1, finish_piece))

            # Top-left diagonal, allowed movement where the final cell is empty
            self.assertTrue(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a-1, row=a+1, piece=finish_piece), piece_1, finish_piece))

            # Not allowed movements. 
            self.assertFalse(Pawn.move_is_possible(None, Cell(column=a+randint(2,8), row=a+randint(2,8), piece=piece_1), Cell(column=a-1, row=a+1, piece=finish_piece), piece_1, finish_piece))
            
            #Diagonal movement where there is an opponent piece
            finish_piece = Piece(player=2, piece_symbol='P', crowned=True)            
            self.assertTrue(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a+1, row=a+1, piece=finish_piece), piece_1, finish_piece))

            #Diagonal movement where there is one of our pieces
            finish_piece = Piece(player=1, piece_symbol='P', crowned=True)            
            self.assertFalse(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a+1, row=a+1, piece=finish_piece), piece_1, finish_piece))

            #Starting and finishing cells are the same
            self.assertFalse(Pawn.move_is_possible(None, Cell(column=a, row=a, piece=piece_1), Cell(column=a, row=a, piece=finish_piece), piece_1, finish_piece))



if __name__ == '__main__':
    unittest.main()
