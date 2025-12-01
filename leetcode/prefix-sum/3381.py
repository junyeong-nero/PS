from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Tracks prefix sums per start-index modulo k while sliding the k-length window,
        so we avoid storing all prefix arrays. Time: O(n), Space: O(k).
        """
        n = len(nums)
        window_sum = sum(nums[:k])
        total_windows = n - k + 1

        prefix_sum = [0] * k  # cumulative sums for each residue group
        min_prefix = [0] * k  # minimum prefix seen so far for each group
        best = float("-inf")

        for idx in range(total_windows):
            if idx:  # slide window by one
                window_sum += nums[idx + k - 1] - nums[idx - 1]

            r = idx % k
            prefix_sum[r] += window_sum
            best = max(best, prefix_sum[r] - min_prefix[r])
            min_prefix[r] = min(min_prefix[r], prefix_sum[r])

        return best
