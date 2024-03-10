class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # m by n matrix
        m = len(matrix)
        n = len(matrix[0])
        boolMap = [[True] * n for _ in range(m)]
        moves = [[0,1],[1,0],[0,-1],[-1,0]]
        res = []
        for col in range(n):
            boolMap[0][col] = False
            res.append(matrix[0][col])
        if m <= 1:
            return res
        for row in range(1,m):
            boolMap[row][n-1] = False
            res.append(matrix[row][n-1])
        if n <= 1:
            return res
        for col in range(n-2,-1,-1):
            boolMap[m-1][col] = False
            res.append(matrix[m-1][col])
        for row in range(m-2,0,-1):
            boolMap[row][0] = False
            res.append(matrix[row][0])
        movesN = 0
        row, col = 1, 0
        if m <= 2 or n <=2:
            return res
        while boolMap[row+moves[movesN][0]][col+moves[movesN][1]] or boolMap[row+moves[(movesN := (movesN+1) % 4)][0]][col+moves[movesN][1]]:
            boolMap[(row := row+moves[movesN][0])][(col := col+moves[movesN][1])] = False
            res.append(matrix[row][col])
        return res