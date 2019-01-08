class Piece:
    def __init__(self, tile, name, isWhite, alive):
        self.tile = tile
        self.name = name
        self.isWhite = isWhite
        self.alive = alive
        self.moves = []
        self.parsedmoves = []
        self.diagonals = [(1,1), (1,-1), (-1,-1), (-1,1)]
        self.cardinals = [(1,0), (0,1), (-1,0), (0,-1)]

    def printMoves(self):
        print(self.name, end = " ")
        for move in self.moves:
            print(move.get_name(), end = " ")
        print()

    def isAlive(self):
        return self.tile != None

    def isWhite(self):
        return self.isWhite

    def setBackPointer(self):
        self.tile.setBackPointer(self)

    def get_piece_tile(self):
        return(self.tile)

    def get_moves(self):
        return self.moves

    def kill_piece(self):
        self.alive = False

    def is_alive(self):
        return self.alive

    def get_name(self):
        return self.name

    def append_parsed_move(self, move):
        self.parsedmoves.append(move)

    def delete_parsed_moves(self):
        self.parsedmoves = []

    def update_moves(self):
        self.moves = self.parsedmoves

    def delete_moves(self):
        self.moves = []

    def new_tile(self, tile):
        self.tile = tile

    def is_in_bounds(self, row, column):
        return(row < 8 and row >= 0 and column < 8 and column >= 0)


    def hit_friendly_piece(self, row, col, board):
        if(not board.is_free(row, col)):
            return(board.piece_isWhite(row, col) == self.isWhite)

    def find_linear_moves(self, row, col, intervals, board):
        for rowint, colint in intervals:
            newrow = row + rowint
            newcol = col + colint
            while(self.is_in_bounds(newrow, newcol)):
                if(board.is_free(newrow, newcol)):
                    self.moves.append(board.get_tile(newrow, newcol))
                else:
                    if(self.hit_friendly_piece(newrow, newcol, board)):
                        break
                    else:
                        self.moves.append(board.get_tile(newrow, newcol))
                        break
                newrow += rowint
                newcol += colint

    def find_point_moves(self, row, col, list, board):
        for rowint, colint in list:
            if(self.is_in_bounds(row+rowint, col+colint) and not self.hit_friendly_piece(row+rowint, col+colint, board)):
                self.moves.append(board.get_tile(row+rowint, col+colint))
