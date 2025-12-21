class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        def get_slope(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            mid = (x1 + x2) * 10000 + (y1 + y2)
            if x1 == x2:
                return 10**9 + 7, x1, mid
            dx = x2 - x1
            dy = y2 - y1
            slope = dy / dx
            y_intercept = (y1 * dx - x1 * dy) / dx
            return slope, y_intercept, mid

        d = defaultdict(list)
        d_mid = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                point1, point2 = points[i], points[j]
                slope, y_intercept, mid = get_slope(point1, point2)
                d[slope].append(y_intercept)
                d_mid[mid].append(slope)

        res = 0
        for y_intercepts in d.values():
            if len(y_intercepts) == 1:
                continue

            total = 0
            counter = Counter(y_intercepts)
            for count in counter.values():
                res += total * count
                total += count

        for slopes in d_mid.values():
            if len(slopes) == 1:
                continue

            total = 0
            counter = Counter(slopes)
            for count in counter.values():
                res -= total * count
                total += count

        return res
