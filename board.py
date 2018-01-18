class Board(object):
    def __init__(self, xsize, ysize):
        self.width  = xsize
        self.height = ysize
        self.board  = [[None for j in range(0, ysize)] for i in range(0, xsize)]


    def move_piece(self, s_loc, e_loc):
        """
        s_loc: (x, y) piece start location
        e_loc: (x, y) piece end location
        """
        if s_loc[0] < 0 or s_loc[0] > self.width or s_loc[1] < 0 or s_loc[1] > self.height:
            raise MoveError("Start location is outside board boundaries " + str(s_loc))


        if e_loc[0] < 0 or e_loc[0] > self.width or e_loc[1] < 0 or e_loc[1] > self.height:
            raise MoveError("End location is outside board boundaries " + str(e_loc))

        if self.board[s_loc[0]][s_loc[1]] is None:
            raise MoveError("No piece at start location " + str(s_loc))

        if self.board[e_loc[0]][e_loc[1]] is not None:
            raise MoveError("Piece exists at end location " + str(e_loc))

        self.board[e_loc[0]][e_loc[1]] = self.board[s_loc[0]][s_loc[1]]
        self.board[s_loc[0]][s_loc[1]] = None


    def add_piece(self, piece, loc):
        """
        piece: piece to add
        loc:   (x, y) location to add piece to
        """
        if self.board[loc[0]][loc[1]] is not None:
            raise PieceError("Can't add piece at location " + str(loc) + " location occupied")
        self.board[loc[0]][loc[1]] = piece


    def __str__(self):
        output = "\n"
        for y in range(0, self.height):
            for x in range(0, self.width):
                output += str(self.board[x][y]) + "\t"
            output += "\n"
        return output


class MoveError(Exception):
    def __init__(self, message):
        self.message = "Can't move piece: " + message


class PieceError(Exception):
    def __init__(self, message):
        self.message = message
