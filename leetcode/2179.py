class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos = {v:i for i, v in enumerate(nums1)}
        res = 0

        for i in range(n):
            x = nums2[i]

            for j in range(i + 1, n):
                y = nums2[j]
                if pos[x] >= pos[y]:
                    continue

                for k in range(j + 1, n):
                    z = nums2[k]
                    if pos[y] >= pos[z]:
                        continue

                    res += 1
        
        return res
