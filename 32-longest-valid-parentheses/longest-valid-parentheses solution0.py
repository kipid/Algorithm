class Solution:
    def longestValidParentheses(self, s: str) -> int:
        step = { "(":1, ")":-1 }
        l, r = 0, len(s)
        while l < r:
            if s[l] == "(":
                break
            l += 1
        while l < r:
            if s[r-1] == ")":
                break
            r -= 1
        maxLen, stepOn = 0, 0
        p = l
        while p < r:
            stepOn += step[s[p]]
            if stepOn == 0:
                leng = p - l + 1
                if leng > maxLen:
                    maxLen = leng
            elif stepOn < 0:
                stepOn, l = 0, p + 1
            p += 1
        p = r - 1
        stepOn = 0
        l = 0
        while l < r:
            if s[l] == "(":
                break
            l += 1
        while l < p:
            stepOn += step[s[p]]
            if stepOn == 0:
                leng = r - p
                if leng > maxLen:
                    maxLen = leng
            elif stepOn > 0:
                stepOn, r = 0, p
            p -= 1
        return maxLen