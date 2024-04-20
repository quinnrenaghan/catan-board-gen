import Board_Utility as Util
import Balanced_Utility as Balanced


while True:
    board = Util.Board()
    result = Balanced.resource_distribution(board)
    if result <= 100:
        print(board)
        break



