class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        maxsum = 0
        
        # Prefix sum array
        sum = [0] * (n + 1)
        for i in range(n):
            sum[i + 1] = sum[i] + nums[i]
        
        # Arrays to store the starting index of left and right max sum intervals
        posLeft = [0] * n
        posRight = [0] * n
        ans = [0] * 3

        # DP for starting index of the left max sum interval
        tot = sum[k] - sum[0]
        for i in range(k, n):
            if sum[i + 1] - sum[i + 1 - k] > tot:
                posLeft[i] = i + 1 - k
                tot = sum[i + 1] - sum[i + 1 - k]
            else:
                posLeft[i] = posLeft[i - 1]

        # DP for starting index of the right max sum interval
        posRight[n - k] = n - k
        tot = sum[n] - sum[n - k]
        for i in range(n - k - 1, -1, -1):
            if sum[i + k] - sum[i] >= tot:
                posRight[i] = i
                tot = sum[i + k] - sum[i]
            else:
                posRight[i] = posRight[i + 1]

        # Test all possible middle intervals
        for i in range(k, n - 2 * k + 1):
            l = posLeft[i - 1]
            r = posRight[i + k]
            tot = (sum[i + k] - sum[i]) + (sum[l + k] - sum[l]) + (sum[r + k] - sum[r])
            if tot > maxsum:
                maxsum = tot
                ans[0], ans[1], ans[2] = l, i, r

        return ans
