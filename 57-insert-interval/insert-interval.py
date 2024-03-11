class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left1, right1 = 0, len(intervals)-1
        left2, right2 = 0, len(intervals)-1
        if len(intervals) == 0:
            return [newInterval]

        def findLeftInterval(left: int, right: int) -> int:
            print(f"findLeft :: {left = }, {right = }")
            if left >= right-1:
                if newInterval[0] <= intervals[left][1]:
                    return left
                else:
                    return right
            mid = (left + right) // 2
            if newInterval[0] <= intervals[mid][1]:
                return findLeftInterval(left, mid)
            else:
                return findLeftInterval(mid, right)
        
        def findRightInterval(left: int, right: int) -> int:
            print(f"findRight :: {left = }, {right = }")
            if left >= right-1:
                if newInterval[1] < intervals[right][0]:
                    return left
                else:
                    return right
            mid = (left + right) // 2
            if newInterval[1] < intervals[mid][0]:
                return findRightInterval(left, mid)
            else:
                return findRightInterval(mid, right)

        if newInterval[0] <= intervals[left1][1]:
            right2 = findRightInterval(left2, right2)
            print(f"{right2 = }")
            if right2 == left2 and newInterval[1] < intervals[left2][0]:
                return [newInterval] + intervals
            else:
                return [[min(intervals[left1][0], newInterval[0]), max(intervals[right2][1], newInterval[1])]] + intervals[right2+1:]
        elif newInterval[0] > intervals[right1][1]:
            return intervals + [newInterval]
        if newInterval[1] < intervals[left2][0]:
            return [newInterval] + intervals
        elif newInterval[1] >= intervals[right2][0]:
            left1 = findLeftInterval(left1, right1)
            if left1 == right1 and newInterval[0] > intervals[right1][1]:
                return intervals + [newInterval]
            else:
                return intervals[:left1] + [[min(intervals[left1][0], newInterval[0]), max(intervals[right2][1], newInterval[1])]]
        
        left1 = findLeftInterval(left1, right1)
        right2 = findRightInterval(left2, right2)
        return intervals[:left1] + [[min(intervals[left1][0], newInterval[0]), max(intervals[right2][1], newInterval[1])]] + intervals[right2+1:]