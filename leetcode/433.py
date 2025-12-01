class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        n = len(startGene)

        def check_diff(a, b):
            count = sum([1 for i in range(n) if a[i] != b[i]])
            return count

        visited = set()

        def dfs(cur, target):
            if cur in visited:
                return float("inf")
            if cur == target:
                return 0

            res = float("inf")
            for gene in bank:
                if check_diff(cur, gene) > 1:
                    continue
                visited.add(cur)
                res = min(res, 1 + dfs(gene, target))
                visited.remove(cur)

            return res

        res = dfs(startGene, endGene)
        return -1 if res == float("inf") else res
