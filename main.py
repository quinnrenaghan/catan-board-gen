import Board_Utility as Util
import Balanced_Utility as Balanced

def get_board(minutes):
    boards_per_second = 10000.00 / 5
    seconds = minutes * 60
    num_boards = int(boards_per_second * seconds)

    best_board = Util.Board()
    best_score = sum(Balanced.balance_score(best_board))

    for num in range(num_boards):
        board = Util.Board()
        score = sum(Balanced.balance_score(board))
        if score < best_score:
            best_score = score
            best_board = board
    return best_board








