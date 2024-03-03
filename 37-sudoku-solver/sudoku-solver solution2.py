class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i: int, j: int, num: str) -> bool:
            for p in range(9):
                if board[p][j] == num:
                    return False
                if board[i][p] == num:
                    return False
            p0 = (i // 3) * 3
            q0 = (j // 3) * 3
            for p in range(3):
                for q in range(3):
                    if board[p0+p][q0+q] == num:
                        return False
            return True

        checker = [ [ {"1","2","3","4","5","6","7","8","9"} for _i in range(9) ] for _j in range(9) ]

        def exclude(i: int, j: int, num: str) -> None:
            board[i][j] = num
            checker[i][j] = set(num)
            for k in range(9):
                checker[k][j].discard(num)
            for l in range(9):
                checker[i][l].discard(num)
            p0 = (i // 3) * 3
            q0 = (j // 3) * 3
            for k in range(3):
                for l in range(3):
                    p = p0 + k
                    q = q0 + l
                    checker[p][q].discard(num)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    exclude(i, j, board[i][j])

        candTuples = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    candTuples.append((len(checker[i][j]), i, j))
        candTuples.sort()

        def solve(k: int):
            if k == len(candTuples):
                return True
            _, i, j = candTuples[k]
            if board[i][j] == ".":
                for num in checker[i][j]:
                    if isValid(i, j, num):
                        board[i][j] = num
                        if solve(k+1):
                            return True
                        else:
                            board[i][j] = "."
                return False
            else:
                return solve(k+1)

        solve(0)