import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        for ch in reversed(s):
            if ch == " ":
                break
            count += 1
        return count
        