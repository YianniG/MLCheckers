class Piece(object):
    def __init__(self, player, loc):
        self.player = player
        player._add_piece(self)
        self.loc = loc

    def get_loc(self):
        return self.loc

    def move(self, loc):
        self.loc = loc

    def get_player(self):
        return self.player

    def __str__(self):
        return str(self.loc)
