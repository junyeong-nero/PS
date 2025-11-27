class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur = sum(nums[:k])
        arr = [cur]

        for i in range(n - k):
            cur -= nums[i]
            cur += nums[i + k]
            arr.append(cur)

        m = len(arr)
        prefix = defaultdict(list)
        for i in range(k):
            if not prefix[i]:
                prefix[i].append(0)
            for j in range(n // k):
                if i + j * k >= m:
                    break
                prefix[i].append(prefix[i][-1] + arr[i + j * k])

        def get_maximum(prefix_arr):
            res = -float("inf")
            if len(prefix_arr) <= 1:
                return res
            cur_min = prefix_arr[0]
            for num in prefix_arr[1:]:
                res = max(res, num - cur_min)
                cur_min = min(cur_min, num)
            return res

        # print(prefix)

        temp = [get_maximum(arr) for arr in prefix.values()]
        # print(temp)
        res = max(temp)
        return res
