class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def count(sIndex: int, tIndex: int) -> int:
            if sIndex < tIndex:
                return 0
            if (sIndex, tIndex) in memo:
                return memo[(sIndex, tIndex)]
            if sIndex == 0 and tIndex == 0:
                memo[(0, 0)] = 1 if s[0]==t[0] else 0
                return memo[(0, 0)]
            if sIndex > 0 and tIndex == 0:
                memo[(sIndex, tIndex)] = count(sIndex-1, 0) + 1 if s[sIndex]==t[0] else count(sIndex-1, 0)
                return memo[(sIndex, tIndex)]
            if s[sIndex] == t[tIndex]:
                memo[(sIndex, tIndex)] = count(sIndex-1, tIndex-1) + count(sIndex-1, tIndex)
                return memo[(sIndex, tIndex)]
            else:
                memo[(sIndex, tIndex)] = count(sIndex-1, tIndex)
                return memo[(sIndex, tIndex)]

        return count(len(s)-1, len(t)-1)