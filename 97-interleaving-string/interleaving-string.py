class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def rec(i1, i2, i3):
            if i1 == len(s1) and i2 == len(s2) and i3 == len(s3):
                return True
            return i3 < len(s3) and (i1 < len(s1) and s1[i1] == s3[i3] and rec(i1+1, i2, i3+1)) or (i2 < len(s2) and s2[i2] == s3[i3] and rec(i1, i2+1, i3+1))
        if len(s3) != len(s1) + len(s2):
            return False
        return rec(0, 0, 0)