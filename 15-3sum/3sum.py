class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        dict_nums = {}
        for i in range(len(nums)):
            if nums[i] == 0:
                if 0 in dict_nums:
                    dict_nums[0].append(i)
                else:
                    dict_nums[0]=[i]
        if 0 in dict_nums and len(dict_nums[0]) >= 3:
            res.append([0,0,0])
        dict_first_num = {}
        for i in range(len(nums)-1, -1, -1):
            dict_first_num[nums[i]] = i
        dict_last_num = {}
        for i in range(len(nums)):
            dict_last_num[nums[i]] = i
        i = 0
        while i < len(nums)-2:
            if dict_first_num[nums[i]] != i:
                i += 1
                continue
            j = i+1
            while j < len(nums)-1:
                numK = -nums[i]-nums[j]
                if numK in dict_last_num:
                    if nums[i] == nums[j] and dict_first_num[nums[j]] + 1 == j:
                        if nums[j] < numK:
                            res.append([nums[i], nums[j], numK])
                    elif dict_first_num[nums[j]] == j:
                        if nums[j] < numK:
                            res.append([nums[i], nums[j], numK])
                        elif nums[j] == numK:
                            if dict_last_num[nums[j]] > j:
                                res.append([nums[i], nums[j], numK])
                j += 1
            i += 1
        return res
