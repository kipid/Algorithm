import re

class Solution:
    def isNumber(self, s: str) -> bool:
        test = False
        pattern00 = re.compile("^[\+\-]?\d+?\.?\d*$")
        pattern01 = re.compile("^[\+\-]?\d*\.?\d+?$")
        pattern0 = re.compile("^[\+\-]?\d+?\.?\d+?[eE][\+\-]?\d+?$")
        pattern1 = re.compile("^[\+\-]?\d*\.?\d+?[eE][\+\-]?\d+?$")
        pattern2 = re.compile("^[\+\-]?\d+?\.?\d*[eE][\+\-]?\d+?$")
        if pattern00.search(s) or pattern01.search(s) or pattern0.search(s) or pattern1.search(s) or pattern2.search(s):
            return True
        return False