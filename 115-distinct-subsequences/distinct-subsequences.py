class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache
        def count(sIndex: int, tIndex: int) -> int:
            if sIndex < 0 or tIndex < 0:
                return 0
            if sIndex < tIndex:
                return 0
            if sIndex == 0 and tIndex == 0:
                return 1 if s[0]==t[0] else 0
            if sIndex > 0 and tIndex == 0:
                return count(sIndex-1, 0) + 1 if s[sIndex]==t[0] else count(sIndex-1, 0)
            if s[sIndex] == t[tIndex]:
                return count(sIndex-1, tIndex-1) + count(sIndex-1, tIndex)
            else:
                return count(sIndex-1, tIndex)

        return count(len(s)-1, len(t)-1)