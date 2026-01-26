class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        indices = [i for i in range(n) if seats[i] == 1]

        res = -1
        if len(indices) >= 1:
            res = max(res, max(indices[0], n - 1 - indices[-1]))

        if len(indices) > 1:
            temp = max(
                [(indices[i + 1] - indices[i]) // 2 for i in range(len(indices) - 1)]
            )
            res = max(res, temp)

        return res
