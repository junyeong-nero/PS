
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        res = 0
        def dist(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

        # dist(points[i], points[j]) = dist(points[i], points[k])
        dist_map = dict()
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points):
                dist_map[(i, j)] = dist(point1, point2)
        print(dist_map)

        n = len(points)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or i == k or j == k:
                        continue

                    a = dist_map[(i, j)]
                    b = dist_map[(i, k)]

                    if a == b:
                        res += 1

        return res