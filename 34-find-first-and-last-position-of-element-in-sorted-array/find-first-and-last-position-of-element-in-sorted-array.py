class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        if len(nums) > 0:
            if nums[left] == target:
                right = left
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left, right - 1]
            elif nums[right] == target:
                left = right
                while left >= 0 and nums[left] == target:
                    left -= 1
                return [left + 1, right]
            elif target < nums[left] or nums[right] < target:
                return [-1, -1]
        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                left = mid
                while left >= 0 and nums[left] == target:
                    left -= 1
                right = mid
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left+1, right-1]
            elif nums[left] == target:
                right = left
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left, right - 1]
            elif nums[right] == target:
                left = right
                while left >= 0 and nums[left] == target:
                    left -= 1
                return [left + 1, right]

            if nums[left] < target < nums[mid]:
                right = mid - 1
            elif nums[mid] < target < nums[right]:
                left = mid + 1
            else:
                return [-1, -1]

        return [-1, -1]