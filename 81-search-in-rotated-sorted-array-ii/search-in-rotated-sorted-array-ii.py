class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right + 1) // 2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
        return nums[left] == target