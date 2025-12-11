class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        x_arr = dict()
        y_arr = dict()

        for i, (x, y) in enumerate(buildings):
            if x not in x_arr:
                x_arr[x] = []
            if y not in y_arr:
                y_arr[y] = []

            heappush(x_arr[x], (y, i))
            heappush(y_arr[y], (x, i))

        def get_candidate(heap):
            res = []
            while heap:
                pos, index = heappop(heap)
                res.append(index)

            return set(res[1:-1]) if len(res) >= 3 else set()

        x_candidates = set()
        for heap in x_arr.values():
            x_candidates |= get_candidate(heap)

        y_candidates = set()
        for heap in y_arr.values():
            y_candidates |= get_candidate(heap)

        # print(x_candidates)
        # print(y_candidates)

        return len(x_candidates & y_candidates)
