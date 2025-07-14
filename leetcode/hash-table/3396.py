class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            counter[nums[i]] += 1
            if counter[nums[i]] == 2:
                return math.ceil((i + 1) / 3)

        return 0
