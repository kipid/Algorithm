import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern0 = re.compile("^[\+\-]?(\d+?\.?\d+?|\d*\.?\d+?|\d+?\.?\d*)([eE][\+\-]?\d+)?$")
        if pattern0.search(s):
            return True
        return False