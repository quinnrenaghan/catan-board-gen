import Board_Utility as util
import time
board = set()

start_time = time.time()
seed = time.time() % 10000
first_board = util.Board(seed)

for key, value in first_board.tile_dict.items():
    print(f"\n{key} : {value}")

