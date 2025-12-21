from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            # need at least two consecutive zeros
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        mods = {0: -1}
        s = 0
        for i, v in enumerate(nums):
            s += v
            mod = s % k
            if mod in mods:
                if i - mods[mod] > 1:
                    return True
            else:
                mods[mod] = i
        return False
