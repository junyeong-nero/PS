class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        def get_time(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            return max(dx, dy)

        res = 0
        n = len(points)

        for i in range(n - 1):
            point1, point2 = points[i], points[i + 1]
            res += get_time(point1, point2)
    
        return res
