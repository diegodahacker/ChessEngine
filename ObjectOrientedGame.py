from Tile import *
from Piece import *
from Pawn import *
from Knight import *
from Bishop import *
from Rook import *
from Queen import *
from King import *

class Board:
    def __init__(self):
        self.tiles = self.maketiles()

    #makes a list of Tile instances
    def maketiles(self):
        tiles = []
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(8):
            placeholder = []
            for j in range(8):
                placeholder.append(Tile(i,j, letters[j]+str(8-i)))
            tiles.append(placeholder)
        return tiles

    def get_tiles(self):
        return self.tiles

    def get_tile(self, row, col):
        return self.tiles[row][col]

    def is_free(self, row, col):
        return self.tiles[row][col].get_piece() is None

    def piece_isWhite(self, row, col):
        return self.tiles[row][col].get_piece().isWhite

    def has_same_color(self, isWhite):
        return

    #def set_tile_piece(self, tile)

BOARD = Board() # global instance

class Game:
    def __init__(self):
        self.int = 0
        self.whitePieces, self.blackPieces = self.makepieces()
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        self.attributeplayers(self.whitePieces, self.blackPieces)
        self.printboard()
        self.main()

    #prints off the every Piece at its location if the Tile has a piece, else it prints "-"
    def printboard(self):
        tiles = BOARD.get_tiles()
        print("     A  B  C  D  E  F  G  H")
        print()
        for i in range(8):
            print(8-i, end = "    ")
            for j in range(8):
                if(tiles[i][j].piece is None):
                    print("-", end = "  ")
                else:
                    print(tiles[i][j].piece.name, end = "  ")
            print()

    #makes a list of WhitePieces and BlackPieces, each with a pointer to the Tile they're on
    def makepieces(self):
        tiles = BOARD.get_tiles()

        whitenames = ["♙", "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
        blacknames = ["♟", "♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        pieces = [Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
        whitePieces = []
        blackPieces = []
        for i in range(8):
            whitePieces.append(Pawn(tiles[6][i], whitenames[0], True, True))
            blackPieces.append(Pawn(tiles[1][i], blacknames[0], False, True))

        for i in range(8):
            whitePieces.append(pieces[i](tiles[7][i], whitenames[i+1], True, True))
            blackPieces.append(pieces[i](tiles[0][i], blacknames[i+1], False, True))

        return whitePieces, blackPieces

        whitePieces[0]

    #assigns a pointer from every Tile that has a piece to its piece
    def attributeplayers(self, whitePieces, blackPieces):
        for piece in whitePieces:
            piece.setBackPointer()
        for piece in blackPieces:
            piece.setBackPointer()

    def findmoves(self, pieces):
        for piece in pieces:
            if(piece is not None):
                piece.delete_moves()
                piece.delete_parsed_moves()
                piece.findmoves(BOARD)

    def printMoves(self, isWhite):
        if(isWhite):
            pieces = self.whitePieces
        else:
            pieces = self.blackPieces
        for piece in pieces:
            if(piece is not None):
                piece.printMoves()
            else:
                print("None")

    def parsemoves(self, isWhite):
        if(isWhite):
            pieces = self.whitePieces
            enemy_pieces = self.blackPieces
        else:
            pieces = self.blackPieces
            enemy_pieces = self.whitePieces
        self.findmoves(pieces)
        for piece in pieces:
            if(piece is not None):
                for move in piece.get_moves():
                    self.testmove(piece, move)
                    update_pieces(enemy_pieces)
                    if(not self.is_in_Check(pieces, enemy_pieces)):
                        piece.append_parsed_move(move)
                    self.reverse_testmove()
                piece.update_moves()

    def testmove(piece, move):
        if(move.has_piece()):
            move.get_piece().kill_piece()
            move.delete_piece()
        move.new_piece(piece)
        piece.new_tile(move)
        piece.get_tile().delete_piece()

    def is_in_Check(pieces, enemy_pieces):
        in_in_Check = False
        self.findmoves(enemy_pieces)
        for piece in enemy_pieces:
            for move in piece.get_moves():
                if(move.get_piece() == pieces[12]):
                    is_in_Check = True
        return(is_in_Check)


    def append_moves(self, pieces):
        moves = []
        for piece in pieces:
            for move in piece.get_moves():
                moves.append(move)
        return moves

    def move_has_king(self, pieces, enemymoves):
        for move in enemymoves:
            if(move.get_piece() == pieces[12]):
                return True
            else:
                return False

    def is_in_Check(self, isWhite):
        if(isWhite):
            pieces = self.whitePieces
            enemy_pieces = self.blackPieces
        else:
            pieces = self.blackPieces
            enemy_pieces = self.whitePieces
        self.findmoves(enemy_pieces)
        enemymoves = self.append_moves(enemy_pieces)
        for move in enemymoves:
            piece = move.get_piece()
            if(piece is not None):
                print(move.name)
                print(piece.get_name())
                print(isWhite)
        if(self.move_has_king(pieces, enemymoves)):
            return True
        else:
            return False

    def is_possible_position(self, input):
        numbers = ["1","2","3","4","5","6","7","8"]
        if(len(input)==2 and input[0] in self.letters and input[1] in numbers):
            return True
        else:
            return False

    def is_possible_move(self, piece, move, pieces):
        if(self.is_possible_position(piece) and self.is_possible_position(move)):
            start_tile = self.convert_pos(piece)
            piece = start_tile.get_piece()
            end_tile = self.convert_pos(move)
            return(piece in pieces and end_tile in piece.moves)

    def convert_pos(self, input):
        lettersdict = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
        letterindex = lettersdict[input[0]]
        numberindex = 8-int(input[1])
        tiles = BOARD.get_tiles()
        return tiles[numberindex][letterindex]

    def main(self):
        white_turn = True
        while(True):
            if(white_turn):
                pieces = self.whitePieces
            else:
                pieces = self.blackPieces
            self.findmoves(pieces)
            self.printMoves(pieces)
            //self.move(white_turn)
            white_turn = not white_turn







ChessGame = Game()
