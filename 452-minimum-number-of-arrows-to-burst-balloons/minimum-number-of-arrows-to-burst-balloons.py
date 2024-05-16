class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(f"{points = }")
        intersections = []
        
        def findIntersection(p1: List[int], p2: List[int]) -> List[int]:
            intersection = [max(p1[0], p2[0]), min(p1[1], p2[1])]
            if intersection[0] > intersection[1]:
                return None
            return intersection

        intersections.append(points[0])
        i = 1
        while i < len(points):
            intersection = findIntersection(intersections[-1], points[i])
            if intersection:
                intersections[-1] = intersection
            else:
                intersections.append(points[i])
            i += 1
        return len(intersections)