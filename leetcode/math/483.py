class Solution:
    def smallestGoodBase(self, n):
        n = int(n)
        # m is the number of '1's minus 1 (the highest power)

        max_m = int(math.log2(n))
        for m in range(max_m, 1, -1):
            # Solve for k: n ≈ k^m  => k ≈ n^(1/m)
            k = int(n ** (1 / m))

            if k > 1:
                # Use the geometric sum formula to verify
                if (k ** (m + 1) - 1) // (k - 1) == n:
                    return str(k)

        return str(n - 1)
