class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        if n < 3:
            return []
        board = [[0 for _ in range(n)] for k in range(n)]

        # board[i][j] = 0 (possible), 1 (attackable), 2 (Queen)
        # Only downward check is enough.
        def downwardCheck(board: List[List[int]], row: int, col: int) -> List[List[int]]:
            newBoard = [[board[i][j] for j in range(n)] for i in range(n)]
            newBoard[row][col] = 2
            for i in range(row+1, n):
                if col - (i - row) >= 0:
                    newBoard[i][col - (i - row)] = 1
                if col + (i - row) < n:
                    newBoard[i][col + (i - row)] = 1
                newBoard[i][col] = 1
            return newBoard
        
        res = []
        def addQueen(board: List[List[int]], row: int) -> bool:
            if row >= n:
                ans0 = [["Q" if board[i][j] == 2 else "." for j in range(n)] for i in range(n)]
                ans1 = []
                for i in range(n):
                    ans1.append("".join(ans0[i]))
                res.append(ans1)
                return True
            addable = False
            for k in range(n):
                if board[row][k] == 0:
                    addable = True
                    break
            # print(board)
            if not addable:
                return False
            addable1 = False
            for k in range(n):
                if board[row][k] == 0:
                    newBoard = downwardCheck(board, row, k)
                    addable2 = addQueen(newBoard, row+1)
                    addable1 = addable1 or addable2
            return addable1
        
        addQueen(board, 0)
        return res
