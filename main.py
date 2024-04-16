import Board_Utility as util
import time
seed = time.time() % 1000

first_board = util.Board(seed)

for value in first_board.tile_dict.values():
    print(f"\n{value}")