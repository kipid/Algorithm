class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted = s.split()
        patternDict = dict()
        patternSet = set()
        if len(splitted) != len(pattern):
            return False
        for i, ch in enumerate(pattern):
            if ch in patternDict:
                if patternDict[ch] != splitted[i]:
                    return False
            else:
                if splitted[i] in patternSet:
                    return False
                patternDict[ch] = splitted[i]
                patternSet.add(splitted[i])
        return True