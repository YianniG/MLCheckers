
from board_maker import *
from board       import *
from player      import *
from utils       import *

board = Board(10, 10)
p1 = Player('1')
p2 = Player('2')
rows_for_each_player = 2
make_std_board(board, rows_for_each_player, p1, p2)

print(board)

print("move piece 0,1 to 1,2")

board.move_piece((0,1), (1,2))

print(board)

print_pieces(p1.get_pieces())
print_pieces(p2.get_pieces())
