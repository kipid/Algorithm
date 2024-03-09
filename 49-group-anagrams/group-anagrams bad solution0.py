class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def isAnagram(str1: dict[str, int], str2: str) -> bool:
            str1Dict = dict(str1)
            isAnag = True
            for i, s2 in enumerate(str2):
                if s2 in str1Dict:
                    str1Dict[s2] -= 1
                    if str1Dict[s2] <= 0:
                        del str1Dict[s2]
                else:
                    isAnag = False
                    break
            return isAnag and len(str1Dict) == 0
        
        res = []
        while len(strs) > 0:
            strsCopy = list(strs)
            group = [strs[0]]
            strsCopy.remove(strs[0])
            str1Dict = dict()
            for i, cha in enumerate(strs[0]):
                if cha in str1Dict:
                    str1Dict[cha] += 1
                else:
                    str1Dict[cha] = 1
            for i in range(1,len(strs)):
                if len(strs[0]) == len(strs[i]) and isAnagram(str1Dict, strs[i]):
                    strsCopy.remove(strs[i])
                    group.append(strs[i])
            res.append(group)
            strs = strsCopy
        return res