import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        for i, ch in enumerate(s[::-1]):
            if ch != " ":
                count += 1
            else:
                break
        return count
        