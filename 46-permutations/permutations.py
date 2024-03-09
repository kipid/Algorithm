class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        set_ = set(nums)
        res = []
        def addNum(setNum: set[int], path: List[int]):
            newSetNum0 = set(setNum)
            for num in newSetNum0:
                path.append(num)
                newSetNum1 = set(newSetNum0)
                newSetNum1.remove(num)
                # print(f"{newSetNum1 = }, {path = }")
                if len(newSetNum1) > 0:
                    addNum(newSetNum1, path)
                else:
                    res.append(list(path))
                path.pop()
        addNum(set_, [])
        return res
