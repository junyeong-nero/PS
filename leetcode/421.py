class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

        max_xor = 0
        mask = 0

        # Iterate from the Most Significant Bit (MSB) down to the Least Significant Bit (LSB).
        # We check 32 bits (range 31 down to 0).
        for i in range(31, -1, -1):

            # The mask grows bit by bit:
            # i=31 -> 1000...000
            # i=30 -> 1100...000
            # ...
            mask |= 1 << i

            # Extract the prefix of each number up to the current bit 'i'.
            # We use a Set for O(1) lookup time.
            prefixes = {num & mask for num in nums}

            # We perform a "Greedy" check.
            # We assume the bit at position 'i' can be 1 in the final result.
            # 'candidate' represents the potential new max_xor if this bit is set to 1.
            candidate = max_xor | (1 << i)

            # Now we check: Does there exist any pair (A, B) in 'prefixes' such that A ^ B = candidate?
            # Using the XOR property: if A ^ B = candidate, then A ^ candidate = B.
            # So, we iterate through prefixes and check if (prefix ^ candidate) exists in the set.
            for prefix in prefixes:
                if (prefix ^ candidate) in prefixes:
                    # If found, it means it is possible to set the i-th bit to 1.
                    # We update max_xor to this candidate.
                    max_xor = candidate
                    break

        return max_xor
