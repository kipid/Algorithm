class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j, sum = 0, 0, len(nums1) + len(nums2)
        mid = sum // 2
        midFound = False
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        if not midFound:
            while i < len(nums1):
                merged.append(nums1[i])
                i += 1
            while j < len(nums2):
                merged.append(nums2[j])
                j += 1
        if sum % 2 == 0:
            return (merged[mid] + merged[mid - 1]) / 2
        else:
            return merged[mid]
