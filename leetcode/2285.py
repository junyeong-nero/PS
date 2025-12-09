class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = Counter()
        for u, v in roads:
            counter[u] += 1
            counter[v] += 1

        cur = n
        res = 0
        for key, freq in counter.most_common():
            res += freq * cur
            cur -= 1
        # print(counter)

        return res
