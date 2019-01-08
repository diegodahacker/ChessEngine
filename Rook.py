from Piece import *

class Rook(Piece):
    def findmoves(self, board):
        self.moves = []
        self.parsedmoves = []
        row = self.tile.row
        col = self.tile.column
        self.find_linear_moves(row, col, self.cardinals, board)
