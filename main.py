import Board_Utility as Util
import Balanced_Utility as Balanced

best_board = Util.Board()
best_score = sum(Balanced.balance_score(best_board))

for num in range(10000):
    board = Util.Board()
    score = sum(Balanced.balance_score(board))
    if score < best_score:
        best_score = score
        best_board = board

print(best_board)
print(best_score)




