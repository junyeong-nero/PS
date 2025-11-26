class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        arr2 = sorted(arr2)
        for num in arr1:
            left = bisect_left(arr2, num - d)
            right = bisect_right(arr2, num + d)
            if right - left <= 0:
                res += 1

        return res
