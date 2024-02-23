class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxL = 1
        l = 1
        dict_ = {s[0:1]:0}
        i = 1
        start = 0
        while i < len(s):
            if s[i:i+1] in dict_:
                l = i - dict_[s[i:i+1]]
                newStart = dict_[s[i:i+1]] + 1
                j = newStart - 1
                while j >= start:
                    del dict_[s[j:j+1]]
                    j -= 1
                dict_[s[i:i+1]] = i
                start = newStart
            else:
                l += 1
                dict_[s[i:i+1]] = i
                if l > maxL:
                    maxL = l
            i += 1
        return maxL
