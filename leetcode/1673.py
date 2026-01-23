class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # a is more competitive than b means:
        #   1. len(a) == len(b) == k
        #   2. a < b
        # => smallest number (subsequence) with k digits

        n = len(nums)
        stack = []
        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) - 1 + n - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack
