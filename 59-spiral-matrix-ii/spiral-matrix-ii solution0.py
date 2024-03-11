class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        boolMap = [[True] * (n+2) for _ in range(n+2)]
        for j in range(n+2):
            boolMap[-1][j] = False
            boolMap[n][j] = False
        for i in range(n):
            boolMap[i][-1] = False
            boolMap[i][n] = False
        moves = [[0,1], [1,0], [0,-1], [-1,0]]
        res = [[0] * n for _ in range(n)]
        count = 1
        row, col = 0, -1
        movesDirection = 0
        while boolMap[row+moves[movesDirection][0]][col+moves[movesDirection][1]] or boolMap[row+moves[(movesDirection := (movesDirection+1)%4)][0]][col+moves[movesDirection][1]]:
            res[row := row+moves[movesDirection][0]][col := col+moves[movesDirection][1]] = count
            boolMap[row][col] = False
            count += 1
        return res