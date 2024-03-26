class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        for n in range(2, numRows+1):
            row = [1]
            for k in range(len(res[-1])-1):
                row += [res[-1][k]+res[-1][k+1]]
            row += [1]
            res.append(row)
        return res