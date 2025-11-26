class Solution:
    def shiftDistance(
        self, s: str, t: str, nextCost: List[int], previousCost: List[int]
    ) -> int:
        n = len(s)

        def shift_chars(char, direct):
            temp = chr(ord(char) + direct)
            index = ord(char) - ord("a")
            cost = nextCost[index] if direct == 1 else previousCost[index]
            if temp < "a":
                temp = "z"
            if temp > "z":
                temp = "a"
            return temp, cost

        def minimum_cost(index):
            source, target = s[index], t[index]

            temp = source
            cost_0 = 0
            while temp != target:
                temp, d_cost = shift_chars(temp, 1)
                cost_0 += d_cost

            temp = source
            cost_1 = 0
            while temp != target:
                temp, d_cost = shift_chars(temp, -1)
                cost_1 += d_cost

            return min(cost_1, cost_0)

        cost = sum([minimum_cost(i) for i in range(n)])
        return cost
