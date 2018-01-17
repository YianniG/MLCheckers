class Piece(object):
    def __init__(self, player):
        self.player = player

    def __str__(self):
        return str(self.player)
