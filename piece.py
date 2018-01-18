class Piece(object):
    def __init__(self, player):
        self.player = player
        player._add_piece(self)

    def __str__(self):
        return str(self.player)
