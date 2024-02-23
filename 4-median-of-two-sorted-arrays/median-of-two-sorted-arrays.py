class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        total_length = len(merged)

        if total_length % 2 == 0:
            mid1 = total_length // 2
            mid2 = mid1 - 1
            median = (merged[mid1] + merged[mid2]) / 2
        else:
            median = merged[total_length // 2]

        return median