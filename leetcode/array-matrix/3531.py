class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        bottom = [n + 1] * (n + 1)  # min col
        top = [0] * (n + 1)  # max col
        left = [n + 1] * (n + 1)  # min row
        right = [0] * (n + 1)  # max row

        # First pass: compute extremes
        for x, y in buildings:
            bottom[x] = min(bottom[x], y)
            top[x] = max(top[x], y)
            left[y] = min(left[y], x)
            right[y] = max(right[y], x)

        # Second pass: count covered
        covered = 0
        for x, y in buildings:
            if bottom[x] < y < top[x] and left[y] < x < right[y]:
                covered += 1
        return covered
