class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (right + left + 1) // 2
            print(f"{left = }, {mid = }, {right = }")
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]: # 왼쪽 부분이 정렬되어 있는 경우
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # 오른쪽 부분이 정렬되어 있는 경우
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        print(f"{left = }")
        return left if nums[left%len(nums)] == target else -1