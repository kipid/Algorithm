class Solution:
    def subsetsWithDup(self, nums: list[int]) -> set[tuple[int]]:
        res = {()}
        dict_ = dict()
        for num in nums:
            dict_[num] = dict_.get(num, 0) + 1
        for key, freq in dict_.items():
            res1 = set(res)
            for item in res1:
                res.update([item + (key,) * k for k in range(freq+1)])
        # res2 = []
        # for item in res:
        #     res2.append(list(item))
        return res