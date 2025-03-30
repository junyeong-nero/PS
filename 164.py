class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        res = 0
        d = deque([nums[0]])
        for i in range(1, n):
            num = nums[i]
            if num > d[-1]:
                d.append(num)
            else:
                d.appendleft(num)
        print(d)

        res = 0
        for i in range(n - 1):
            diff = d[i + 1] - d[i]
            res = max(res, diff)

        return res