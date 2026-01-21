class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:

        def dist(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

        def find(query):
            x, y, r = query
            res = 0
            for point in points:
                if dist(point, (x, y)) <= r**2:
                    res += 1

            return res

        return [find(q) for q in queries]
