class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        n = len(nums)
        end = n - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[end]:  # Fail to estimate which side is sorted
                end -= 1
            elif nums[mid] > nums[end]: # Left side is sorted
                if nums[start] <= target and target < nums[mid]:    # Check if target in left side
                    end = mid - 1
                else:   # Otherwise check the unsorted side
                    start = mid + 1
            else:   # Right side is sorted
                if nums[mid] < target and target <= nums[end]:      # Check if target is in right side
                    start = mid + 1
                else:
                    end = mid - 1
        return False