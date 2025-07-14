class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0

        pairs = []
        for i in range(n - 1):
            pairs.append(weights[i] + weights[i + 1])

        pairs.sort()

        min_sum = sum(pairs[: k - 1])
        max_sum = sum(pairs[n - k :])

        return max_sum - min_sum
