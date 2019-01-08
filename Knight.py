from Piece import *

class Knight(Piece):
    def findmoves(self, board):
        self.moves = []
        self.parsedmoves = []
        row = self.tile.row
        col = self.tile.column
        list = [(-2,1), (2,1), (-2,-1), (2,-1), (1,-2), (1,2), (-1,-2), (-1,2)]
        self.find_point_moves(row, col, list, board)
