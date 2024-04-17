class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s0Index = -1
        for s0 in s:
            s0Index = t.find(s0, s0Index+1)
            if s0Index == -1:
                return False
        return True