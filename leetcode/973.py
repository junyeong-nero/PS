class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(arr):
            x, y = arr
            return x**2 + y**2

        points = sorted(points, key=dist)
        return points[:k]
