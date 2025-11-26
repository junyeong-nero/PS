class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: List[int], previousCost: List[int]
    ) -> int:
        n = len(s)

        def distance(source, target):
            target = ord(target) - ord("a")
            source = ord(source) - ord("a")
            return (target - source + 26) % 26, (source - target + 26) % 26

        cost = 0
        for i in range(n):
            d_next, d_prev = distance(s[i], t[i])
            cost_next = nextCost[ord(s[i]) - ord("a")] * d_next
            cost_prev = previousCost[ord(s[i]) - ord("a")] * d_prev
            print(i, cost_next, cost_prev)
            cost += min(cost_next, cost_prev)

        return cost
