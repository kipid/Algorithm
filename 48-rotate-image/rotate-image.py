class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        (0,0) (0,1) (0,2) ... (0,n-1)
        (1,0) (1,1) ...       (1,n-1)
        (2,0) (2,1) ...       (2,n-1)
        (3,0) (3,1) ...       (3,n-1)
        (4,0) (4,1) ...       (4,n-1)
        ...
        (n-1,0) (n-1,1) ...   (n-1,n-1)
        """
        n = len(matrix)
        for offset in range(0, n//2):
            for i in range(offset, n-1-offset):
                matrix[offset][i], matrix[n-1-i][offset], matrix[n-1-offset][n-1-i], matrix[i][n-1-offset] = matrix[n-1-i][offset], matrix[n-1-offset][n-1-i], matrix[i][n-1-offset], matrix[offset][i]
