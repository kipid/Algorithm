class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        # row = index // n
        # col = index % n
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        while left < right:
            mid = (left + right + 1) // 2
            print(f"{left = }, {right = }, {mid = }")
            if matrix[mid // n][mid % n] <= target:
                left = mid
            else:
                right = mid - 1
        if matrix[left // n][left % n] == target:
            return True
        return False