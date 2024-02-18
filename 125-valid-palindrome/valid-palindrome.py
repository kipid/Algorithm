import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strReplaced = re.sub(r"[^a-zA-Z0-9]+", "", s).lower()
        return strReplaced == strReplaced[::-1]
