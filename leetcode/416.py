class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
            
        n = len(nums)

        def func(target):
            if target == 0:
                return True
            if target < 0:
                return False

            res = False
            for i in range(n):
                if nums[i] == 0:
                    continue
                temp, nums[i] = nums[i], 0
                if func(target - temp):
                    return True
                nums[i] = temp

            return False
        
        return func(total // 2)
