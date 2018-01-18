from piece import Piece

def make_std_board(board, rows, player1, player2):
    """
    :param board:   Board to add to
    :param rows:    The number fo rows of inital checkers for each player
    :param player1: Player1
    :param player2: Player2
    :return: None
    """
    # Player 1
    for row in range(0, rows):
        for i in range((row + 1) % 2, board.width, 2):
            # First row
            loc = (i, row)
            board.add_piece(Piece(player1, loc))

    # Player 2
    for row in range(0, rows):
        for i in range(row % 2, board.width, 2):
            loc = (i, board.height-1-row)
            board.add_piece(Piece(player2, loc))

