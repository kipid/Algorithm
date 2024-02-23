class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        locs = {}
        l = r = 0
        longest = 0
        for r, letter in enumerate(s):
            if letter in locs and locs[letter] >= l:
                l = locs[letter] + 1
            longest = max(longest, r - l + 1)
            locs[letter] = r
        return longest