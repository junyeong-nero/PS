class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [item for item, value in counter.items() if value >= 2]
