import Board_Utility as util
import time

seed = time.time() % 10000
first_board = util.Board(seed)
print(first_board)

