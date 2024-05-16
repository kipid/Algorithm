class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = {}
        for i, num in enumerate(nums):
            if num in window:
                if i - window[num] <= k:
                    return True
            window[num] = i
        return False