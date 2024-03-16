board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
boardCopy = list(board)
board[0][0] = "Z"
print(f"{board = }\n{boardCopy = }")

import copy

boardDeepCopy = copy.deepcopy(board)
board[0][0] = "100"
print(f"{board = }\n{boardDeepCopy = }")
