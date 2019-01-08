class Tile:
    def __init__(self, row, column, name):
        self.row = row
        self.column = column
        self.name = name
        self.piece = None

    def setBackPointer(self, newPiece):
        self.piece = newPiece

    def new_piece(self, new_piece):
        self.piece = new_piece

    def delete_piece(self):
        self.piece = None

    def get_piece(self):
        return self.piece

    def get_row(self):
        return self.row

    def get_name(self):
        return self.name

    def get_row_col(self):
        return self.row, self.column

    def has_piece(self):
        return(self.piece is not None)
