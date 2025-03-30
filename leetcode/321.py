class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        arr = nums1 + nums2
        m, n = len(nums1), len(nums2)

        def func(index, value, count):
            if count == 0:
                return value

            res = value
            for i in range(index, m + n):
                num = arr[i]
                res = max(res, func(i + 1, value * 10 + num, count - 1))
            return res
        
        res = func(0, 0, k)
        return [int(x) for x in str(res)]
