class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        k = 0
        while k < len(intervals):
            left0, right0 = intervals[k][0], intervals[k][1]
            maxRight = right0
            k += 1
            while k < len(intervals):
                left1, right1 = intervals[k][0], intervals[k][1]
                if maxRight >= left1:
                    maxRight = max(maxRight, right1)
                    k += 1
                else:
                    break
            res.append([left0, maxRight])
        return res