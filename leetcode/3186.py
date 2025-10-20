class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = Counter(power)
        keys = sorted(list(counter.keys()))
        n = len(keys)

        def dfs(index=0, lower_bound=-1):
            temp = 0
            for i in range(index, n):
                key = keys[i]
                if key <= lower_bound:
                    continue
                temp = max(temp, key * counter[key] + dfs(i + 1, keys[i] + 2))
            return temp

        result = dfs()
        print(result)
        return result
