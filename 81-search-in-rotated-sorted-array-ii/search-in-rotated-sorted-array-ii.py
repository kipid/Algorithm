class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]: # Fail to estimate which side is sorted
                right -= 1
                continue
            if nums[left] == nums[mid]: # Fail to estimate which side is sorted
                left += 1
                continue
            if nums[left] < nums[mid]: # Left side is sorted
                if nums[left] <= target < nums[mid]: # Check if target in left side
                    right = mid - 1
                else: # Otherwise check the unsorted side
                    left = mid
            else: # Right side is sorted
                if nums[mid] < target <= nums[right]: # Check if target is in right side
                    left = mid + 1
                else:
                    right = mid
        return nums[left] == target