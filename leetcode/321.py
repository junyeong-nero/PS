class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        
        @lru_cache(None)
        def func(index1, index2, count):
            if count == 0:
                return ""
            
            max_res = "-1"
            for i in range(index1, m):
                max_res = max(max_res, str(nums1[i]) + func(i + 1, index2, count - 1), key = lambda x: int(x))
            for j in range(index2, n):
                max_res = max(max_res, str(nums2[j]) + func(index1, j + 1, count - 1), key = lambda x: int(x))
            return "" if max_res == "-1" else max_res
        
        res = func(0, 0, k)
        return [int(x) for x in res]
