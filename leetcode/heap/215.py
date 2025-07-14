class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        arr = []
        for num in nums:
            heappush(arr, -num)

        res = 0
        for _ in range(k):
            res = -heappop(arr)
        return res
