class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)

        dp = dict()

        def find(cur):
            if cur in dp:
                return dp[cur]
            res = cur
            for node in graph[cur]:
                temp = find(node)
                if quiet[temp] < quiet[res]:
                    res = temp
            dp[cur] = res
            return res

        res = []
        for i in range(n):
            res.append(find(i))

        return res
