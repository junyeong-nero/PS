class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        a, b = m - 1, n - 1
        i = m + n - 1

        while i >= 0:
            x = nums1[a] if a >= 0 else -float("inf")
            y = nums2[b] if b >= 0 else -float("inf")

            if x > y:
                nums1[i] = x
                a -= 1
            else:
                nums1[i] = y
                b -= 1
            i -= 1
