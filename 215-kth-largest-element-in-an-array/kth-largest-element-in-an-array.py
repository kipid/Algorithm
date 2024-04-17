class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxHeapify(i, n):
            left = 2*i + 1
            right = 2*i + 2
            largest = i
            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                maxHeapify(largest, n)
        
        for i in range((len(nums)-2)//2, -1, -1):
            maxHeapify(i, len(nums))
        for i in range(len(nums)-1, len(nums)-k, -1):
            nums[i], nums[0] = nums[0], nums[i]
            maxHeapify(0, i)
        return nums[0]