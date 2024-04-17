import re

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        splitted = re.split(r"\s+", s)
        return " ".join(reversed(splitted))