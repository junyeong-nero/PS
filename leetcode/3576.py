class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        a, b = nums.count(1), nums.count(-1)
        res = False

        def flip(target):
            arr = nums[:]
            i = 0
            count = 0
            while i < n - 1:
                if arr[i] == target:
                    i += 1
                    continue

                j = i
                while j < n - 1:
                    arr[j] *= -1
                    arr[j + 1] *= -1
                    count += 1
                    if arr[j] == target and arr[j + 1] == target:
                        break
                    j += 1

                i = j + 1
            
            return count <= k


        if a % 2 == 0:
            res |= flip(-1)
        
        if not res and b % 2 == 0:
            res |= flip(1)

        return res
        