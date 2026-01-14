class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        events = []

        squares = sorted(squares, key=itemgetter(0))
        for idx, (x, y, l) in enumerate(squares):
            events.append((y, idx, True))
            events.append((y + l, idx, False))

        events = sorted(events, key=itemgetter(0))
        current = set()  # current handling boxes
        prev_y = events[0][0]

        def func(current_box, dy):
            if dy == 0:
                return 0

            boundary = []
            for idx in sorted(current_box):
                x, y, l = squares[idx]
                if boundary and boundary[-1][1] > x:
                    boundary[-1][1] = max(boundary[-1][1], x + l)
                else:
                    boundary.append([x, x + l])

            return sum([b - a for a, b in boundary])

        area = 0
        area_history = []

        for y, idx, add in events:
            dy = y - prev_y
            dx = func(current, dy)
            area_history.append((area, dx, dy, prev_y))
            area += dx * dy

            if add:
                current.add(idx)
            else:
                current.remove(idx)

            # print(y, area)
            prev_y = y

        target = area / 2
        i = bisect_left(area_history, target, key=itemgetter(0)) - 1
        # print(area_history[i])

        area, dx, dy, prev_y = area_history[i]
        res = prev_y + (target - area) / dx

        return res
