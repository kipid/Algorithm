class Solution:
    unknown = 81
    def __init__(self):
        self.unknown = 81

    def exclude(self, board: list[list[str]], checker: list[list[set[str]]], num: str, i: int, j: int) -> None:
        if board[i][j] != ".":
            return
        board[i][j] = num
        checker[i][j] = set(num)
        self.unknown -= 1
        for k in range(9):
            # if num in checker[k][j]:
            checker[k][j].discard(num)
                # if len(checker[k][j]) == 1:
                #     self.exclude(board, checker, checker[k][j].pop(), k, j)
        for l in range(9):
            # if num in checker[i][l]:
            checker[i][l].discard(num)
                # if len(checker[i][l]) == 1:
                #     self.exclude(board, checker, checker[i][l].pop(), i, l)
        p0 = i // 3 * 3
        q0 = j // 3 * 3
        for k in range(3):
            for l in range(3):
                p = p0 + k
                q = q0 + l
                # if num in checker[p][q]:
                checker[p][q].discard(num)
                    # if len(checker[p][q]) == 1:
                    #     self.exclude(board, checker, checker[p][q].pop(), p, q)

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        checker = [ [ {"1","2","3","4","5","6","7","8","9"} for i in range(9) ] for j in range(9) ]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    self.exclude(board, checker, board[i][j], i, j)
        while self.unknown > 0:
            for i in range(9):
                for j in range(9):
                    if board[i][j] == "." and len(checker[i][j]) == 1:
                        self.exclude(board, checker, checker[i][j].pop(), i, j)

board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
sol.solveSudoku(board)
print(board)
