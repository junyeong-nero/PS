class Solution:

    def kthCharacter(self, k, operations):
        mutations = 0
        # Iterate from log2(k) down to 0
        # The int(math.log2(k)) handles k=1 correctly (log2(1) = 0)
        for op in range(int(math.log2(k)), -1, -1):
            # Check if k is greater than 2 raised to the power of op
            if k > (1 << op):
                k -= 1 << op
                mutations += operations[op]

        return chr(ord("a") + mutations % 26)
