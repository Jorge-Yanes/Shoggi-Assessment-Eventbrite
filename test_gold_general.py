import unittest
from gold_general import *
from random import randint

class TestClass(unittest.TestCase):

    # Test cases with allowed moves
    def test_move_is_possible(self):
        for a in range(8):
            # Piece that we are going to move
            piece_1 = Piece(player=1, piece_symbol='G',crowned=False)

            # Piece at the final position
            finish_piece = None

            # One cell fordward, allowed movement where the final cell is empty
            self.assertTrue(Gold_General.move_is_possible(None, Cell(column=a, row=a ), Cell(column=a, row=a+1 ), piece_1, finish_piece))

            # One cell backward, allowed movement where the final cell is empty
            self.assertTrue(Gold_General.move_is_possible(None, Cell(column=a, row=a ), Cell(column=a, row=a-1 ), piece_1, finish_piece))
 
            # One cell to the right, allowed movement where the final cell is empty
            self.assertTrue(Gold_General.move_is_possible(None, Cell(column=a, row=a ), Cell(column=a+1, row=a ), piece_1, finish_piece))
            
            # One cell to the left, allowed movement where the final cell is empty
            self.assertTrue(Gold_General.move_is_possible(None, Cell(column=a, row=a ), Cell(column=a-1, row=a ), piece_1, finish_piece))

            # Top-right diagonal, allowed movement where the final cell is empty
            self.assertTrue(Gold_General.move_is_possible(None, Cell(column=a, row=a ), Cell(column=a+1, row=a+1 ), piece_1, finish_piece))

            # Top-left diagonal, allowed movement where the final cell is empty
            self.assertTrue(Gold_General.move_is_possible(None, Cell(column=a, row=a ), Cell(column=a-1, row=a+1 ), piece_1, finish_piece))

            # Bottom-right diagonal, not allowed movement where the final cell is empty
            self.assertFalse(Gold_General.move_is_possible(None, Cell(column=a, row=a  ), Cell(column=a+1, row=a-1  ), piece_1, finish_piece))

            # Bottom-left diagonal, not allowed movement where the final cell is empty
            self.assertFalse(Gold_General.move_is_possible(None, Cell(column=a, row=a  ), Cell(column=a-1, row=a-1  ), piece_1, finish_piece))

            # Not allowed movements. 
            self.assertFalse(Gold_General.move_is_possible(None, Cell(column=a+randint(2,8), row=a+randint(2,8) ), Cell(column=a-1, row=a+1 ), piece_1, finish_piece))

            #Diagonal movement where there is an opponent piece
            finish_piece = Piece(player=2, piece_symbol='P', crowned=False)            
            self.assertTrue(Gold_General.move_is_possible(None, Cell(column=a, row=a ), Cell(column=a+1, row=a+1 ), piece_1, finish_piece))

            #Diagonal movement where there is one of our pieces
            finish_piece = Piece(player=1, piece_symbol='P',crowned=False)            
            self.assertFalse(Gold_General.move_is_possible(None, Cell(column=a, row=a ), Cell(column=a+1, row=a+1 ), piece_1, finish_piece))

            #Starting and finishing cells are the same
            self.assertFalse(Gold_General.move_is_possible(None, Cell(column=a, row=a ), Cell(column=a, row=a ), piece_1, finish_piece))


if __name__ == '__main__':
    unittest.main()
