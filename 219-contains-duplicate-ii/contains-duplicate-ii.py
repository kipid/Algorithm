class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictN = defaultdict(list)
        for n in range(len(nums)):
            dictN[nums[n]].append(n)
        for n in dictN:
            if len(dictN[n]) > 1:
                for i in range(len(dictN[n])-1):
                    if dictN[n][i+1] - dictN[n][i] <= k:
                        return True
        return False