class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = len(nums)
        index, count = 0, 0
        for i in range(n):
            if nums[i] == val:
                count += 1
                continue
            nums[index] = nums[i]
            index += 1

        # print(nums)
        return n - count