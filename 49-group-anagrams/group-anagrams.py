class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsDict = dict()
        for str0 in strs:
            sortedStr0 = "".join(sorted(str0))
            if sortedStr0 in strsDict:
                strsDict[sortedStr0].append(str0)
            else:
                strsDict[sortedStr0] = [str0]
        # res = []
        # for key, str0 in strsDict.items():
        #     res.append(strsDict[key])
        # return res
        return list(strsDict.values())