class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1, n2 = len(nums1), len(nums2)

        i, j = bisect_left(nums1, 0), bisect_left(nums2, 0)
        # print(i, j)

        nums1_neg, nums1_pos = nums1[:i], nums1[i:]
        nums2_neg, nums2_pos = nums2[:j], nums2[j:]

        # neg, pos
        arr = []
        for neg in nums1_neg:
            for pos in nums2_pos:
                arr.append(neg * pos)
        for neg in nums2_neg:
            for pos in nums1_pos:
                arr.append(neg * pos)

        arr = sorted(arr)
        # print(arr)
        if len(arr) >= k:
            # print("here!")
            return arr[k - 1]
        else:
            k -= len(arr)

        # neg, neg
        arr = []
        for neg in nums1_neg:
            for pos in nums2_neg:
                arr.append(neg * pos)
        # pos, pos
        for neg in nums2_pos:
            for pos in nums1_pos:
                arr.append(neg * pos)

        arr = sorted(arr)
        # print(arr)
        if len(arr) >= k:
            # print("here2!")
            return arr[k - 1]
        else:
            k -= len(arr)

        return
