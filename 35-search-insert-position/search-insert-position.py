class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        if target < nums[left]:
            return left
        elif target > nums[right]:
            return right + 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        if target < nums[left]:
            return left
        else:
            return left + 1