import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.sub(r"\*+", ".*", re.sub(r"\?", ".", p))
        pattern = "^" + pattern + "$"
        # print(pattern)
        pattern = re.compile(pattern)

        revPattern = re.sub(r"\*+", "*.", re.sub(r"\?", ".", p))
        revPattern = "^" + revPattern[::-1] + "$"
        # print(revPattern)
        revPattern = re.compile(revPattern)
        return revPattern.search(s[::-1]) != None and pattern.search(s) != None

sol = Solution()
s = "abaabaaaabbabbaaabaabababbaabaabbabaaaaabababbababaabbabaabbbbaabbbbbbbabaaabbaaaaabbaabbbaaaaabbbabb"
p = "ab*aaba**abbaaaa**b*b****aa***a*b**ba*a**ba*baaa*b*ab*"
print(f"{sol.isMatch(s, p) = }")
