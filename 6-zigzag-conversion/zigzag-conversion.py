class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        i = 0
        step = 1
        array = []
        for _ in range(numRows):
            array.append([])
        for c in s:
            array[i].append(c)
            i += step
            if i == numRows - 1 or i == 0:
                step *= -1
        for i in range(numRows):
            res += "".join(array[i])
        return res