from Piece import *

class Pawn(Piece):
    def findmoves(self, board):
        self.moves = []
        self.parsedmoves = []
        row = self.tile.row
        col = self.tile.column
        if(self.isWhite):
            initial_row = 6
            small_step = 1
            big_step = 2
            bool = False
        else:
            initial_row = 1
            small_step = -1
            big_step = -2
            bool = True

        if(board.is_free(row-small_step, col)):
            self.moves.append(board.get_tile(row-small_step, col))
            if(board.get_tile(row, col).get_row() == initial_row and board.is_free(row-small_step, col) and board.is_free(row-big_step, col)):
                self.moves.append(board.get_tile(row-big_step, col))
        if(col < 7):
            if(board.is_free(row-small_step, col+1) == False and board.piece_isWhite(row-small_step, col+1) == bool):
                self.moves.append(board.get_tile(row-small_step, col+1))
        if(col > 0):
            if(board.is_free(row-small_step, col-1) == False and board.piece_isWhite(row-small_step, col-1) == bool):
                self.moves.append(board.get_tile(row-small_step, col-1))
