class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        q = deque(nums[:3])
        n = len(nums)
        res = 0
        for i in range(3, n):
            # print(q)
            if q[0] + q[2] == q[1] / 2:
                res += 1
            q.popleft()
            q.append(nums[i])

        if q[0] + q[2] == q[1] / 2:
            res += 1

        return res
