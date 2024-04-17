class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictStoT = dict()
        sToTSet = set()
        for i, ch in enumerate(s):
            if ch in dictStoT:
                if dictStoT[ch] != t[i]:
                    return False
            else:
                if t[i] in sToTSet:
                    return False
                dictStoT[ch] = t[i]
                sToTSet.add(t[i])
        return True