class Player(object):
    def __init__(self, name):
        self.name = name
        self.pieces = []

    def make_move(self):
        pass

    def get_pieces(self):
        return self.pieces

    def _add_piece(self, piece):
        self.pieces.append(piece)

    def __str__(self):
        return self.name
