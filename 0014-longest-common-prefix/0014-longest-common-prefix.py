class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return
        minLength = math.inf
        for str in strs:
            minLength = min(minLength, len(str))
        
        res = 0
        for i in range(0, minLength):
            letter = strs[0][i:i+1]
            same = True
            for str in strs:
                if str[i:i+1] != letter:
                    same = False
                    break
            if not same:
                return strs[0][0:i]
        return strs[0][0:minLength]