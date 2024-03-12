class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # nOfPaths[m][n] = nOfPaths[m-1][n] + nOfPaths[m][n-1]
        # if obstacleGrid[m][n] => nOfPaths[m][n]=0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        nOfPaths = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0]:
            return 0
        nOfPaths[0][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j]:
                nOfPaths[0][j] = 0
            else:
                nOfPaths[0][j] = nOfPaths[0][j-1]
        for i in range(1, m):
            if obstacleGrid[i][0]:
                nOfPaths[i][0] = 0
            else:
                nOfPaths[i][0] = nOfPaths[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    nOfPaths[i][j] = 0
                else:
                    nOfPaths[i][j] = nOfPaths[i-1][j] + nOfPaths[i][j-1]
        return nOfPaths[m-1][n-1]
