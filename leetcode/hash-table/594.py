class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(
            [0]
            + [
                (counter[key] + counter[key + 1])
                for key in counter
                if counter[key + 1] > 0
            ]
        )
