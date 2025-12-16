class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:

        tree = defaultdict(list)
        for u, v in hierarchy:
            tree[u].append(v)

        future = [0] + future
        present = [0] + present

        # @cache
        def dfs(ID, discount, left_budget):
            res = 0
            price = (present[ID] // 2) if discount else present[ID]
            # print(ID, discount, left_budget, benefit)

            # if purchase
            if left_budget >= price:
                left_budget -= price
                benefit = future[ID] - price
                for employee in tree[ID]:
                    benefit += dfs(employee, True, left_budget)
                res = max(res, benefit)
                left_budget += price

            # if not purchase
            for employee in tree[ID]:
                res = max(res, dfs(employee, False, left_budget))

            return res

        res = dfs(1, False, budget)
        return res


# 50 - 6 => 44
# 48 - 2 = 46
# 17 - 11 = 6
# 96
