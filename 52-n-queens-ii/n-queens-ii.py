class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        colSet = set()
        posDiag = set()
        negDiag = set()

        def addQueen(row: int):
            if row >= n:
                nonlocal res
                res += 1
                return
            for col in range(n):
                if col in colSet or (col-row) in posDiag or (col+row) in negDiag:
                    continue
                colSet.add(col)
                posDiag.add(col-row)
                negDiag.add(col+row)
                addQueen(row+1)
                colSet.remove(col)
                posDiag.remove(col-row)
                negDiag.remove(col+row)
        
        addQueen(0)
        return res