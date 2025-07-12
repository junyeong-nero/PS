class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = sorted(nums1)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:

        # print(self.nums1)
        # print(self.nums2)

        res = 0
        for num in self.nums2:
            left = bisect_left(self.nums1, tot - num)
            right = bisect_right(self.nums1, tot - num)
            res += right - left

        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
