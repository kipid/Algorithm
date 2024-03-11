import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        pattern = re.compile("\w+$")
        return len(pattern.search(s).group(0))
        