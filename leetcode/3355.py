class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        def check(index):
            return sum([1 for query in queries if query[0] <= index <= query[1]])

        for index, num in enumerate(nums):
            if check(index) < num:
                return False

        return True
