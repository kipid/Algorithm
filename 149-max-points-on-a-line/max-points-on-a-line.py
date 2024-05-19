class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        dict_ = [dict() for _ in range(n-1)]
        for i in range(n-1):
            for j in range(i+1, n):
                if (points[j][0]-points[i][0]) == 0:
                    dict_[i][math.inf] = dict_[i].get(math.inf, 1) + 1
                else:
                    slope = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                    dict_[i][slope] = dict_[i].get(slope, 1) + 1
        max_ = [max(dict_[i].values()) for i in range(n-1)]
        return max(max_)