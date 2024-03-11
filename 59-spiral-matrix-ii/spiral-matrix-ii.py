class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        left, right, top, bottom = 0, n, 0, n
        temp = 1
        while left < right and top < bottom:
            for i in range(left, right):
                res[top][i] = temp
                temp += 1
            top += 1
            right -= 1
            for i in range(top, bottom):
                res[i][right] = temp
                temp += 1
            # if left >= right or top >= bottom:
            #     break
            bottom -= 1
            for i in range(right - 1, left - 1, -1):
                res[bottom][i] = temp
                temp += 1
            for i in range(bottom - 1, top - 1, -1):
                res[i][left] = temp
                temp += 1
            left += 1
        return res
