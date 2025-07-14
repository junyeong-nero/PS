class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        n = len(tops)
        counter = defaultdict(set)
        for i, v in enumerate(tops):
            counter[v].add(i)
        for i, v in enumerate(bottoms):
            counter[v].add(i)
        # print(counter)

        targets = [key for key, value in counter.items() if len(value) == n]
        # print(targets)

        res = float("inf")
        for target in targets:
            res = min(res, n - tops.count(target), n - bottoms.count(target))

        return -1 if res == float("inf") else res
