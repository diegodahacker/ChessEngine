#import stuff
import os
from termcolor import cprint
from copy import copy, deepcopy

#takes in a board and prints it with its off nicely
def printboard(board):
    print()
    for i in range(8):
        print(str(i+1)+"  ", end = " ")
        for j in range(8):
            print(board[i][j], end = " ")
        print()
    print()
    print("    A  B  C  D  E  F  G  H")
    print()


#places the pieces on the board
def placepieces():
    #make the piecesboard and insert - into all the slots
    piecesboard=[]
    placeholder=[]
    for i in range(8):
        for j in range(8):
            placeholder.append("--")
        piecesboard.append(placeholder)
        placeholder=[]

    #insert pawns in second and seventh row
    for i in range(8):
        piecesboard[1][i]="WP"
        piecesboard[6][i]="BP"

    #insert pieces into first and eigth row
    pieces1 = ["R","N","B","Q","K","B","N","R"]
    for i in range(8):
        piecesboard[0][i]="W"+pieces1[i]
        piecesboard[7][i]="B"+pieces1[i]

    return piecesboard

piecesboard = placepieces()
whitepieces = ["WP", "WR","WN", "WB", "WQ", "WK"]
blackpieces = ["BP", "BR","BN", "BB", "BQ", "BK"]
#piecesboard[0][6] = "--"
#piecesboard[0][5] = "--"
printboard(piecesboard)
whitetomove = True
whitekingmoved = False
blackkingmoved = False
a1rookmoved = False
h1rookmoved = False
a8rookmoved = False
h8rookmoved = False

#Every possible move has an object of the move class, storing the old and new position
class Move:
    def __init__(self, column, row, newcolumn, newrow, newname):
        self.column = column
        self.row = row
        self.newcolumn = newcolumn
        self.newrow = newrow
        self.newname = newname


#converts a position from column and row format to chess format
def convertmove(column, row):
    position = ""
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(8):
        if(row == i):
            position += letters[i]
    for i in range(8):
        if(column == i):
            position += str(i+1)
    return position

def convertrow(row):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(8):
        if(row == i):
            position = letters[i]

    return position

def getpossiblemoves(board, color):
    possiblemoves = []
    pieces = []
    enemypieces = []
    if(color=="white"):
        pieces = whitepieces
        enemypieces = blackpieces
    else:
        pieces = blackpieces
        enemypieces = whitepieces

    #checks possible moves
    for column in range(8):
        for row in range(8):
            if board[column][row] in pieces:

                #checks the possible moves for pawns
                if(board[column][row]==pieces[0]):
                    if(color=="white"):
                        if(column<6):
                            if(board[column+1][row] == "--"):
                                possiblemoves.append(Move(column, row, column+1, row, "P"))
                        if(column == 6):
                            if(board[column+1][row]=="--"):
                                possiblemoves.append(Move(column, row, column+1, row, "P"))
                        if(column==1):
                            if(board[column+1][row] == "--" and board[column+2][row] == "--"):
                                possiblemoves.append(Move(column, row, column+2, row, "P"))
                        if(column<6 and row > 0):
                            if(board[column+1][row-1] in enemypieces):
                                possiblemoves.append(Move(column, row, column+1, row-1, "P"))
                        if(column==6 and row > 0):
                            if(board[column+1][row-1] in enemypieces):
                                possiblemoves.append(Move(column, row, column+1, row-1, "P"))
                        if(column<6 and row < 7):
                            if(board[column+1][row+1] in enemypieces):
                                possiblemoves.append(Move(column, row, column+1, row+1, "P"))
                        if(column==6 and row < 7):
                            if(board[column+1][row+1] in enemypieces):
                                possiblemoves.append(Move(column, row, column+1, row+1, "P"))
                    else:
                        if(column>1):
                            if(board[column-1][row] == "--"):
                                possiblemoves.append(Move(column, row, column-1, row, "P"))
                        if(column == 1):
                            if(board[column-1][row]=="--"):
                                possiblemoves.append(Move(column, row, column-1, row, "P"))
                        if(column==6):
                            if(board[column-1][row] == "--" and board[column-2][row] == "--"):
                                possiblemoves.append(Move(column, row, column-2, row, "P"))
                        if(column>1 and row > 0):
                            if(board[column-1][row-1] in enemypieces):
                                possiblemoves.append(Move(column, row, column-1, row-1, "P"))
                        if(column==1 and row > 0):
                            if(board[column-1][row-1] in enemypieces):
                                possiblemoves.append(Move(column, row, column-1, row-1, "P"))
                        if(column>1 and row < 7):
                            if(board[column-1][row+1] in enemypieces):
                                possiblemoves.append(Move(column, row, column-1, row+1, "P"))
                        if(column==1 and row < 7):
                            if(board[column-1][row+1] in enemypieces):
                                possiblemoves.append(Move(column, row, column-1, row+1, "P"))

                #checks the possible moves for the Rook
                if(board[column][row]==pieces[1]):
                    if(column<7):
                        for i in range(column+1, 8):
                            if(board[i][row] not in pieces):
                                possiblemoves.append(Move(column, row, i, row, "R"))
                                if(board[i][row] in enemypieces):
                                    break
                            else:
                                break

                    if(column>0):
                        for i in range(column-1, -1, -1):
                            if(board[i][row] not in pieces):
                                possiblemoves.append(Move(column, row, i, row, "R"))
                                if(board[i][row] in enemypieces):
                                    break
                            else:
                                break

                    if(row<7):
                        for i in range(row+1, 8):
                            if(board[column][i] not in pieces):
                                possiblemoves.append(Move(column, row, column, i, "R"))
                                if(board[column][i] in enemypieces):
                                    break
                            else:
                                break

                    if(row>0):
                        for i in range(row-1, -1, -1):
                            if(board[column][i] not in pieces):
                                possiblemoves.append(Move(column, row, column, i, "R"))
                                if(board[column][i] in enemypieces):
                                    break
                            else:
                                break

                #checks the possible moves for the Knight
                if(board[column][row]==pieces[2]):
                    if(column<6 and row>0 and board[column+2][row-1] not in pieces):
                        possiblemoves.append(Move(column, row, column+2, row-1, "N"))
                    if(column<6 and row<7 and board[column+2][row+1] not in pieces):
                        possiblemoves.append(Move(column, row, column+2, row+1, "N"))
                    if(column<7 and row>1 and board[column+1][row-2] not in pieces):
                        possiblemoves.append(Move(column, row, column+1, row-2, "N"))
                    if(column>0 and row>1 and board[column-1][row-2] not in pieces):
                        possiblemoves.append(Move(column, row, column-1, row-2, "N"))
                    if(column>1 and row>0 and board[column-2][row-1] not in pieces):
                        possiblemoves.append(Move(column, row, column-2, row-1, "N"))
                    if(column>1 and row<7 and board[column-2][row+1] not in pieces):
                        possiblemoves.append(Move(column, row, column-2, row+1, "N"))
                    if(column>0 and row<6 and board[column-1][row+2] not in pieces):
                        possiblemoves.append(Move(column, row, column-1, row+2, "N"))
                    if(column<7 and row<6 and board[column+1][row+2] not in pieces):
                        possiblemoves.append(Move(column, row, column+1, row+2, "N"))

                #checks the possible moves for the Bishop
                if(board[column][row]==pieces[3]):
                    #down right
                    if(column<7 and row<7):
                        if(8-column<8-row):
                            int = 1
                            for i in range(column+1, 8):
                                if(board[i][row+int] not in pieces):
                                    possiblemoves.append(Move(column, row, i, row+int, "B"))
                                    if(board[i][row+int] in enemypieces):
                                        break
                                    int +=1
                                else:
                                    break
                        else:
                            int = 1
                            for i in range(row+1, 8):
                                if(board[column+int][i] not in pieces):
                                    possiblemoves.append(Move(column, row, column+int, i, "B"))
                                    if(board[column+int][i] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break


                    if(column>0 and row>0):
                        #up left
                        if(column>row):
                            int = 1
                            for i in range(row-1,-1,-1):
                                if(board[column-int][i] not in pieces):
                                    possiblemoves.append(Move(column, row, column-int, i, "B"))
                                    if(board[column-int][i] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break

                        else:
                            int = 1
                            for i in range(column-1,-1,-1):
                                if(board[i][row-int] not in pieces):
                                    possiblemoves.append(Move(column, row, i, row-int, "B"))
                                    if(board[i][row-int] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break


                    if(column<7 and row>0):
                        #down left
                        if(8-column<row):
                            int = 1
                            for i in range(column+1,8):
                                if(board[i][row-int] not in pieces):
                                    possiblemoves.append(Move(column, row, i, row-int, "B"))
                                    if(board[i][row-int] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break

                        else:
                            int = 1
                            for i in range(row-1,-1,-1):
                                if(board[column+int][i] not in pieces):
                                    possiblemoves.append(Move(column, row, column+int, i, "B"))
                                    if(board[column+int][i] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break


                    if(column>0 and row<7):
                        #up right
                        if(8-row<column):
                            int = 1
                            for i in range(row+1,8):
                                if(board[column-int][i] not in pieces):
                                    possiblemoves.append(Move(column, row, column-int, i, "B"))
                                    if(board[column-int][i] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break

                        else:
                            int = 1
                            for i in range(column-1,-1,-1):
                                if(board[i][row+int] not in pieces):
                                    possiblemoves.append(Move(column, row, i, row+int, "B"))
                                    if(board[i][row+int] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break

                #checks possible moves for Queen
                if(board[column][row]==pieces[4]):
                    #copy of bishop
                    #down right
                    if(column<7 and row<7):
                        if(8-column<8-row):
                            int = 1
                            for i in range(column+1, 8):
                                if(board[i][row+int] not in pieces):
                                    possiblemoves.append(Move(column, row, i, row+int, "Q"))
                                    if(board[i][row+int] in enemypieces):
                                        break
                                    int +=1
                                else:
                                    break
                        else:
                            int = 1
                            for i in range(row+1, 8):
                                if(board[column+int][i] not in pieces):
                                    possiblemoves.append(Move(column, row, column+int, i, "Q"))
                                    if(board[column+int][i] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break


                    if(column>0 and row>0):
                        #up left
                        if(column>row):
                            int = 1
                            for i in range(row-1,-1,-1):
                                if(board[column-int][i] not in pieces):
                                    possiblemoves.append(Move(column, row, column-int, i, "Q"))
                                    if(board[column-int][i] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break

                        else:
                            int = 1
                            for i in range(column-1,-1,-1):
                                if(board[i][row-int] not in pieces):
                                    possiblemoves.append(Move(column, row, i, row-int, "Q"))
                                    if(board[i][row-int] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break


                    if(column<7 and row>0):
                        #down left
                        if(8-column<row):
                            int = 1
                            for i in range(column+1,8):
                                if(board[i][row-int] not in pieces):
                                    possiblemoves.append(Move(column, row, i, row-int, "Q"))
                                    if(board[i][row-int] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break

                        else:
                            int = 1
                            for i in range(row-1,-1,-1):
                                if(board[column+int][i] not in pieces):
                                    possiblemoves.append(Move(column, row, column+int, i, "Q"))
                                    if(board[column+int][i] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break


                    if(column>0 and row<7):
                        #up right
                        if(8-row<column):
                            int = 1
                            for i in range(row+1,8):
                                if(board[column-int][i] not in pieces):
                                    possiblemoves.append(Move(column, row, column-int, i, "Q"))
                                    if(board[column-int][i] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break

                        else:
                            int = 1
                            for i in range(column-1,-1,-1):
                                if(board[i][row+int] not in pieces):
                                    possiblemoves.append(Move(column, row, i, row+int, "Q"))
                                    if(board[i][row+int] in enemypieces):
                                        break
                                    int+=1
                                else:
                                    break


                    #copy of Rook
                    if(column<7):
                        for i in range(column+1, 8):
                            if(board[i][row] not in pieces):
                                possiblemoves.append(Move(column, row, i, row, "Q"))
                                if(board[i][row] in enemypieces):
                                    break
                            else:
                                break

                    if(column>0):
                        for i in range(column-1, -1, -1):
                            if(board[i][row] not in pieces):
                                possiblemoves.append(Move(column, row, i, row, "Q"))
                                if(board[i][row] in enemypieces):
                                    break
                            else:
                                break

                    if(row<7):
                        for i in range(row+1, 8):
                            if(board[column][i] not in pieces):
                                possiblemoves.append(Move(column, row, column, i, "Q"))
                                if(board[column][i] in enemypieces):
                                    break
                            else:
                                break

                    if(row>0):
                        for i in range(row-1, -1, -1):
                            if(board[column][i] not in pieces):
                                possiblemoves.append(Move(column, row, column, i, "Q"))
                                if(board[column][i] in enemypieces):
                                    break
                            else:
                                break

                #checks possible moves for King
                if(board[column][row]==pieces[5]):
                    if(column<7):
                        if(board[column+1][row] not in pieces):
                            possiblemoves.append(Move(column, row, column+1, row, "K"))
                    if(column>0):
                        if(board[column-1][row] not in pieces):
                            possiblemoves.append(Move(column, row, column-1, row, "K"))
                    if(row<7):
                        if(board[column][row+1] not in pieces):
                            possiblemoves.append(Move(column, row, column, row+1, "K"))
                    if(row>0):
                        if(board[column][row-1] not in pieces):
                            possiblemoves.append(Move(column, row, column, row-1, "K"))
                    if(column<7 and row<7):
                        if(board[column+1][row+1] not in pieces):
                            possiblemoves.append(Move(column, row, column+1, row+1, "K"))
                    if(column<7 and row>0):
                        if(board[column+1][row-1] not in pieces):
                            possiblemoves.append(Move(column, row, column+1, row-1, "K"))
                    if(column>0 and row<7):
                        if(board[column-1][row+1] not in pieces):
                            possiblemoves.append(Move(column, row, column-1, row+1, "K"))
                    if(column>0 and row>0):
                        if(board[column-1][row-1] not in pieces):
                            possiblemoves.append(Move(column, row, column-1, row-1, "K"))
                    if(color == "white" and whitekingmoved == False and h1rookmoved == False):
                        print(column, row)
                        if(board[column][row+1] == "--" and board[column][row+2] == "--"):
                            possiblemoves.append(Move(column, row, column, row+2, "C"))
                            #castleKS = True
                            #print("possiblemoves: "+str(castleKS))
                    if(color == "white" and whitekingmoved == False and a1rookmoved == False):
                        if(board[column][row-1] == "--" and board[column][row-2] == "--" and board[column][row-3]=="--"):
                            possiblemoves.append(Move(column, row, column, row-2, "C"))
                            #castleQS = True
                    if(color == "black" and blackkingmoved == False and a8rookmoved == False):
                        if(board[column][row-1] == "--" and board[column][row-2] == "--" and board[column][row-3]=="--"):
                            possiblemoves.append(Move(column, row, column, row-2, "C"))
                            #castleQS = True
                    if(color == "black" and blackkingmoved == False and h8rookmoved == False):
                        if(board[column][row+1] == "--" and board[column][row+2] == "--"):
                            possiblemoves.append(Move(column, row, column, row+2, "C"))
                            #castleKS = True


    return possiblemoves

#used for check --> test to see if this move would get you out of check
def testmove(board, column, row, newcolumn, newrow, newname, color):
    board[column][row]="--"
    str = color[0]
    board[newcolumn][newrow]= str.upper() + newname

#checks if one side is in check
def incheck(board, color):
    isincheck = False
    if(color == "white"):
        enemymoves = getpossiblemoves(board, "black")
        pieces = whitepieces
    else:
        enemymoves = getpossiblemoves(board, "white")
        pieces = blackpieces

    for i in enemymoves:
        if(board[i.newcolumn][i.newrow]==pieces[5]):
            isincheck = True

    return isincheck

#finds the moves to get you out of check if incheck == True
def parsemoves(board, color):
    if(incheck(board, color)):
        if(color == "white"):
            pieces = whitepieces
        else:
            pieces = blackpieces

    moves = getpossiblemoves(board, color)
    newmoves = []
    for i in moves:
        testboard = deepcopy(board)
        testmove(testboard, i.column, i.row, i.newcolumn, i.newrow, i.newname, color)
        if(not incheck(testboard, color)):
            newmoves.append(i)

    return newmoves

#prints all possible moves without considering check
def printpossiblemoves(board, color):
    print()
    possiblemoves = getpossiblemoves(board, color)
    int = 1
    for i in range(len(possiblemoves)):
        print(possiblemoves[i].newname+convertmove(possiblemoves[i].newcolumn, possiblemoves[i].newrow), end=" ")
        if(int%20 == 0):
            print()
        int += 1

    print()
    print("Number of Moves: " + str(len(possiblemoves)))

#prints all moves considering check
def printparsedmoves(board, color):
    print()
    possiblemoves = parsemoves(board, color)
    int = 1
    for i in possiblemoves:
        print(i.newname+convertmove(i.newcolumn, i.newrow), end=" ")
        if(int%20 == 0):
            print()
        int += 1

    print()
    print("Number of Moves: " + str(len(possiblemoves)))

#asks for input and moves the piece if the move is in parsedmoves
def move(board, color, moves):
    global whitekingmoved
    global blackkingmoved
    #whitekingmoved=True
    piece = input("Piece: ").upper()
    newpiece = input("Move: ").upper()
    printparsedmoves(board, color)
    #piece = piece.upper()
    #newpiece = newpiece.upper()
    #moves = parsemoves(board, color)
    success = False
    for i in moves:
        if(piece == "CASTLE" and i.newname == "C"):
            if(newpiece == "KING SIDE" and i.newrow == 6):
                print("ICE CREAM")
                board[i.column][i.row]="--"
                board[i.newcolumn][i.newrow]=color[0].upper()+"K"
                board[i.newcolumn][7]="--"
                board[i.newcolumn][5]=color[0].upper()+"R"
                if(color == "white"):
                    whitekingmoved = True
                    h1rookmoved = True
                    print("move: "+str(whitekingmoved))
                else:
                    blackkingmoved = True
                    h8rookmoved = True
            elif(newpiece == "QUEEN SIDE" and i.newrow == 2):
                board[i.column][i.row]="--"
                board[i.newcolumn][i.newrow]==color[0].upper()+"K"
                board[i.newcolumn][0]="--"
                board[i.newcolumn][3]=color[0].upper()+"R"
                if(color == "white"):
                    whitekingmoved = True
                    a1rookmoved = True
                else:
                    blackkingmoved = True
                    a8rookmoved = True
            else:
                print("Not a possible move. Try again...")
                move(board, color, moves)

        else:
            whitekingmoved=True
            if(convertmove(i.column, i.row)==piece and convertmove(i.newcolumn, i.newrow)==newpiece):
                success = True
                column=i.column
                row=i.row
                newcolumn=i.newcolumn
                newrow=i.newrow
                name=i.newname
                if(color == "white"):
                    lastcolumn = 7
                else:
                    lastcolumn = 0
                if(name == "P" and newcolumn==lastcolumn):
                    name = input("What do you want to promote to?").upper()
                    i.newname = name
                    possibleinputs = ["Q", "N", "B", "R"]
                    while(name not in possibleinputs):
                        print("Not a possible promotion. Try again...")
                        name = input("What do you want to promote to?").upper()
                        i.newname = name
                if(success):
                    board[column][row]="--"
                    board[newcolumn][newrow]=color[0].upper()+name
                    printboard(board)
                else:
                    print("Not a possible move. Try again...")
                    move(board, color, moves)


while(True):
    if(whitetomove):
        moves = parsemoves(piecesboard, "white")
        if(len(moves)== 0):
            print("Black Wins!!!")
            break
        else:
            print("White to move...")
            move(piecesboard, "white", moves)
            print("while loop: "+str(whitekingmoved))
            whitetomove = False
    else:
        moves = parsemoves(piecesboard, "black")
        if(len(moves)==0):
            print("White Wins!!!")
            break
        else:
            print("Black to move...")
            move(piecesboard, "black", moves)
            whitetomove = True
