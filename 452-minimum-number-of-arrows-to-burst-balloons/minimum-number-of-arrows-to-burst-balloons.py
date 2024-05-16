class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 1
        points.sort(key = lambda x:x[1])
        print(f"{points = }")
        first_end = points[0][1]
        # this is to count non-overlapping intervals:
        # so it doesn't matter if you use points[1:] or points
        for start, end in points[1:]:
            if start > first_end:
                first_end = end
                arrows +=1
        return arrows