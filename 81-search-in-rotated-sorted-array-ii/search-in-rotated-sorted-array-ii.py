class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        numsSet = set(nums)
        return target in numsSet