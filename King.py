from Piece import *

class King(Piece):
    def findmoves(self, board):
        self.moves = []
        self.parsedmoves = []
        row = self.tile.row
        col = self.tile.column
        list = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        self.find_point_moves(row, col, list, board)
