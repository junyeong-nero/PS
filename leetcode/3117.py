class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)

        def dfs(index, and_index, sum_value=0, history=[]):
            if and_index == m and index == n:
                # print(history, sum_value)
                return sum_value
            if and_index >= m or index >= n:
                return float("inf")

            candidates = []
            i, cur = index, nums[index]
            while i < n:
                cur = cur & nums[i]
                if cur == andValues[and_index]:
                    candidates.append(i)
                i += 1

            res = float("inf")
            for candidate in candidates:
                temp = dfs(
                    candidate + 1,
                    and_index + 1,
                    sum_value + nums[candidate],
                    history + [nums[index : candidate + 1]],
                )
                res = min(res, temp)
            return res

        res = dfs(0, 0)
        return -1 if res == float("inf") else res
