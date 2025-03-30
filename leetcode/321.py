class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        m, n = len(nums1), len(nums2)

        @cache
        def func(index1, index2, value, count):
            if count == 0:
                return value

            res = value
            for i in range(index1, m):
                res = max(res, func(i + 1, index2, value * 10 + nums1[i], count - 1))

            for j in range(index2, n):
                res = max(res, func(index1, j + 1, value * 10 + nums2[j], count - 1))

            return res
        
        res = func(0, 0, 0, k)
        return [int(x) for x in str(res)]
