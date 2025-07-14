from itertools import deque


class Solution:

    def continuousSubarrays(self, nums):
        maxQ = deque()
        minQ = deque()
        left = 0
        res = 0

        for right in range(len(nums)):
            while maxQ and nums[maxQ[-1]] < nums[right]:
                maxQ.pop()

            maxQ.append(right)

            while minQ and nums[minQ[-1]] > nums[right]:
                minQ.pop()

            minQ.append(right)

            while nums[maxQ[0]] - nums[minQ[0]] > 2:
                if maxQ[0] < minQ[0]:
                    left = maxQ[0] + 1
                    maxQ.popleft()
                else:
                    left = minQ[0] + 1
                    minQ.popleft()

            res += right - left + 1

        return res

    def continuousSubarrays(self, nums) -> int:
        n = len(nums)
        i, j = 0, 0
        res = 0

        # O(n^2)
        for i in range(n):
            temp_min = nums[i]
            temp_max = nums[i]
            for j in range(i, n):
                temp_min = min(temp_min, nums[j])
                temp_max = max(temp_max, nums[j])

                if temp_max - temp_min <= 2:
                    res += 1
                else:
                    break

        return res
