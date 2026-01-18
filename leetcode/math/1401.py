class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:

        def dist(point1, point2):
            a, b = point1
            c, d = point2
            return (a - c) ** 2 + (b - d) ** 2

        points = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        boundary = [x1 - radius, y1 - radius, x2 + radius, y2 + radius]
        if boundary[0] <= xCenter <= boundary[2] and y1 <= yCenter <= y2:
            return True
        if x1 <= xCenter <= x2 and boundary[1] <= yCenter <= boundary[3]:
            return True

        arr = [dist(point, (xCenter, yCenter)) for point in points]
        if any([elem <= radius**2 for elem in arr]):
            return True

        return False
