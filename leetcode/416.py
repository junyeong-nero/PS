class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False

        @cache
        def func(index, target):
            if target == 0:
                return True
            if target < 0:
                return False

            for i in range(index, n):
                if nums[i] == 0:
                    continue
                temp, nums[i] = nums[i], 0
                if func(index + 1, target - temp):
                    return True
                nums[i] = temp

            return False
        
        return func(0, total // 2)