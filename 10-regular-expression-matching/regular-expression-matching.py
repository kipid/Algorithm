import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = re.sub(r"\*+", "*", p)
        pattern = re.compile("^"+p+"$")
        return pattern.search(s) is not None
