class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        counter = Counter(nums)
        return [key for key, value in counter.items() if value == n][0]
