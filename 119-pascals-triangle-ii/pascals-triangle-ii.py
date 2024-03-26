class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @lru_cache
        def helper(n: int) -> List[int]:
            if n==0:
                return [1]
            res = [1]
            preList = helper(n-1)
            for k in range(len(preList)-1):
                res.append(preList[k]+preList[k+1])
            res.append(1)
            return res
        
        return helper(rowIndex)