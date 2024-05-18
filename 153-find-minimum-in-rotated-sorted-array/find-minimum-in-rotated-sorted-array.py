class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(left: int, right: int):
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            else:
                if nums[mid] < nums[right]:
                    return helper(left, mid)
                else:
                    return helper(mid+1, right)
        
        return helper(0, n-1)