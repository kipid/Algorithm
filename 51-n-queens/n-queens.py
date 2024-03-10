class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n < 3:
            return []
        board = [["."] * n for _ in range(n)]
        colSet = set()
        posDiag = set()
        negDiag = set()
        res = []

        def addQueen(row: int):
            if row >= n:
                ans0 = []
                for k in range(n):
                    ans0.append("".join(board[k]))
                res.append(ans0)
                return
            for col in range(n):
                if col in colSet or (col-row) in posDiag or (col+row) in negDiag:
                    continue
                board[row][col] = "Q"
                colSet.add(col)
                posDiag.add(col-row)
                negDiag.add(col+row)
                addQueen(row+1)
                board[row][col] = "."
                colSet.remove(col)
                posDiag.remove(col-row)
                negDiag.remove(col+row)
        
        addQueen(0)
        return res