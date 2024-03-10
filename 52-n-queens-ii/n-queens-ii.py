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
                posD = col-row
                negD = col+row
                if col in colSet or posD in posDiag or negD in negDiag:
                    continue
                colSet.add(col)
                posDiag.add(posD)
                negDiag.add(negD)
                addQueen(row+1)
                colSet.remove(col)
                posDiag.remove(posD)
                negDiag.remove(negD)
        
        addQueen(0)
        return res