class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0

        def dist(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

        # dist(points[i], points[j]) = dist(points[i], points[k])
        # dist_map = dict()
        dist_map = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                point1, point2 = points[i], points[j]
                d = dist(point1, point2)

                dist_map[d].append((i, j))
                
        print(dist_map)

        for key, rows in dist_map.items():
            m = len(rows)
            for i in range(m):
                for j in range(i + 1, m):
                    a, b = rows[i], rows[j]
                    if len(set(a) | set(b)) == 3:
                        res += 2

        return res