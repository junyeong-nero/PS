class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        res = 0
        # n = 100
        # k = 55

        his_index = -1
        his = None

        def dfs(cur, bound):
            if cur > bound:
                return 0

            nonlocal his_index, his
            his_index += 1
            if his_index == k:
                his = cur

            count = 1
            for i in range(10):
                if cur == 0 and i == 0:
                    continue
                count += dfs(cur * 10 + i, bound)

            return count
        

        dfs(0, n)
        print(his_index, his)

        return his