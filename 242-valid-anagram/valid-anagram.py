class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS = dict()
        for i, ch in enumerate(s):
            dictS[ch] = dictS.get(ch, 0) + 1
        for i, ch in enumerate(t):
            if ch in dictS:
                dictS[ch] -= 1
                if dictS[ch] < 0:
                    return False
            else:
                return False
        return True