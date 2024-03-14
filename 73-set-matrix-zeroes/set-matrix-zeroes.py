class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colSet = set()
        rowSet = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    colSet.add(j)
                    rowSet.add(i)
        for col in colSet:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        for row in rowSet:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
