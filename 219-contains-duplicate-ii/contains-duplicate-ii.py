class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        recent_indices = {}
        for i, num in enumerate(nums):
            if num not in recent_indices:
                recent_indices[num] = i
            else:
                distance = i - recent_indices[num]
                if distance <= k:
                    return True
                else:
                    recent_indices[num] = i
        return False