class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        subPs = self.generateParenthesis(n-1)
        res = []
        setP = set()
        for subP in subPs:
            for i in range(len(subP)):
                newP = subP[:i] + "()" + subP[i:]
                if newP not in setP:
                    setP.add(newP)
                    res.append(newP)
        return res
