class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictMag = dict()
        for i, ch in enumerate(magazine):
            dictMag[ch] = dictMag.get(ch, 0) + 1
        for i, ch in enumerate(ransomNote):
            if ch in dictMag:
                dictMag[ch] -= 1
                if dictMag[ch] < 0:
                    return False
            else:
                return False
        return True