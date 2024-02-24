import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        pattern = re.compile("^[\+\-]?\d+")
        i = pattern.search(s)
        if i:
            i = int(i.group(0))
        else:
            i = 0
        if i < -2**31:
            return -2**31
        elif i > 2**31 - 1:
            return 2**31 - 1
        else:
            return i