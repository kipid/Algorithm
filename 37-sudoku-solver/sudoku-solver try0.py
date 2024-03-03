class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        checker = [ [ {"1","2","3","4","5","6","7","8","9"} for i in range(9) ] for j in range(9) ]

        def exclude(num: str, i: int, j: int) -> None:
            board[i][j] = num
            checker[i][j] = set(num)
            for k in range(9):
                checker[k][j].discard(num)
                if len(checker[k][j]) == 1:
                    exclude(checker[k][j].pop(), k, j)
            for l in range(9):
                checker[i][l].discard(num)
                if len(checker[i][l]) == 1:
                    exclude(checker[i][l].pop(), i, l)
            p0 = i // 3 * 3
            q0 = j // 3 * 3
            for k in range(3):
                for l in range(3):
                    p = p0 + k
                    q = q0 + l
                    checker[p][q].discard(num)
                    if len(checker[p][q]) == 1:
                        exclude(checker[p][q].pop(), p, q)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    exclude(board[i][j], i, j)

        candTuples = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    candTuples.append((len(checker[i][j]), i, j))
        candTuples.sort()

        k = 0
        while k < len(candTuples):
            length, i, j = candTuples[k]
            while length == 1:
                exclude(checker[i][j].pop(), i, j)
                k += 1
            candTuples = []
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        candTuples.append((len(checker[i][j]), i, j))
            k = 0
            candTuples.sort()

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
