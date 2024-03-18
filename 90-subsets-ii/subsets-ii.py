class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = {()}
        dict_ = dict()
        for num in nums:
            dict_[num] = dict_.get(num, 0) + 1
        for key, freq in dict_.items():
            res1 = set(res)
            for k in range(freq+1):
                for item in res1:
                    res.add(item + (key,) * k)
        res2 = []
        for item in res:
            res2.append(list(item))
        return res