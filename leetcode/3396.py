class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums)

        res = 0
        for i in range(0, n, 3):
            if set(counter.values()) == {1}:
                return res
            counter -= Counter(nums[i:min(n, i + 3)])
            res += 1
        
        return res