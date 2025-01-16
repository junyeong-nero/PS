class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        n1, n2 = len(nums1), len(nums2)
        if n2 % 2 == 1:
            for num in nums1:
                res = res ^ num 
        if n1 % 2 == 1: 
            for num in nums2:
                res = res ^ num 
        return res