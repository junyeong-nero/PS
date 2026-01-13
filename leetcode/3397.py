class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:

        # 겹치는 것들을 어떻게 처리?
        # stack from minimum

        nums = sorted(nums)
        d = [float("-inf")]

        for num in nums:
            temp = max(d[-1] + 1, num - k)
            if temp > num + k:
                continue
            d.append(temp)

        # print(nums)
        # print(d[1:])

        return len(d) - 1
