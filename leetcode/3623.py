class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        MOD = 10**9 + 7

        def get_slope(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            if x1 == x2:
                return float("inf"), float("inf")
            slope = (y2 - y1) / (x2 - x1)
            y_intercept = slope * (-x1) + y1
            return slope, y_intercept

        d = defaultdict(dict)

        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                point1, point2 = points[i], points[j]
                slope, y_intercept = get_slope(point1, point2)
                if y_intercept not in d[slope]:
                    d[slope][y_intercept] = 0
                d[slope][y_intercept] += 1

        d_sum = dict()
        for slope, slope_info in d.items():
            d_sum[slope] = sum(slope_info.values())

        print(d)
        print(d_sum)

        res = 0
        for slope, slope_info in d.items():
            temp = 0
            for y_intercept, count in slope_info.items():
                temp += (d_sum[slope] - count) * count
            temp = temp // 2
            res = (res + temp) % MOD

        return res
