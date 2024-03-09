class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dict_ = dict()
        for num in nums:
            if num in dict_:
                dict_[num] += 1
            else:
                dict_[num] = 1
        res = []
        
        def addNum(dictNums: dict, path: list[int]):
            dictNums0 = dict(dictNums)
            for num, count in dictNums0.items():
                newDictNums = dict(dictNums0)
                newDictNums[num] -= 1
                path.append(num)
                if newDictNums[num] == 0:
                    del newDictNums[num]
                # print(f"{newDictNums = }, {path = }")
                if len(newDictNums) > 0:
                    addNum(newDictNums, path)
                else:
                    res.append(list(path))
                path.pop()
            
        addNum(dict_, [])
        return res