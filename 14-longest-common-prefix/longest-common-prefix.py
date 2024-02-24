class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        common = strs[0]
        for s in strs[1:]:
            length = min(len(common), len(s))
            i = 0
            while i < length:
                if common[i] != s[i]:
                    break
                i += 1
            common = common[:i]
            if len(common) == 0:
                break
        return common