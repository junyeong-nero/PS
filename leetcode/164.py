class Solution:
    def maximumGap(self, nums):
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo:
            return hi - lo

        B = defaultdict(list)
        for num in nums:
            ind = n - 2 if num == hi else (num - lo) * (n - 1) // (hi - lo)
            B[ind].append(num)
        # print(B)

        cands = [[min(B[i]), max(B[i])] for i in range(n - 1) if B[i]]
        # print(cands)

        return max(y[0] - x[1] for x, y in zip(cands, cands[1:]))
