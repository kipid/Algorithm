class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxL = 0
        l = 0
        dict_ = {}
        i = 0
        start = 0
        for i, letter in enumerate(s):
            if letter in dict_:
                l = i - dict_[letter]
                j = dict_[letter] - 1
                while j >= start:
                    del dict_[s[j:j+1]]
                    j -= 1
                start = dict_[letter] + 1
            else:
                l += 1
                if l > maxL:
                    maxL = l
            dict_[letter] = i
            i += 1
        return maxL
