class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        start, max_len = 0, 1

        for i in range(1, len(s)):
            l, r = i-max_len, i+1
            s1 = s[l-1:r] # +2 check
            s2 = s[l:r] # +1 check

            if l >= 1 and s1 == s1[::-1]:
                start = l-1
                max_len += 2
            elif s2 == s2[::-1]:
                start = l
                max_len += 1
        
        return s[start: start+max_len]