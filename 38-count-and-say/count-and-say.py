class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        k = 1
        count = 1
        s0 = s[0:1]
        res = ""
        while k < len(s):
            if s[k:k+1] == s0:
                count +=1
            else:
                res += str(count) + s0
                s0 = s[k:k+1]
                count = 1
            k += 1
        res += str(count) + s0
        return res