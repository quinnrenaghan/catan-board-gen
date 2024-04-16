import Board_Utility as util
import time
board = set()


for i in range(1000):
    seed = time.time() % 10000 + i
    board.add(util.Board(seed))

