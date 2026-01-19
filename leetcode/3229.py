class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        counter = 0
        prev = 0
        for i in range(len(target)):
            val = target[i] - nums[i]
            if val > prev:
                counter += val - prev

            prev = val

        if prev < 0:
            counter -= prev

        return counter
