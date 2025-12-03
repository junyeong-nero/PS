class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # xor operations
        print(bin(1000)[2:])

        def hamming_distance(a, b):
            temp = a ^ b
            return bin(temp)[2:].count("1")

        # dist(a, b) = dist(b, a)

        # dist(a, b) + dist(a, c) = dist(a ^ b, 0) + dist(a ^ c, 0)
        #                           dist(a ^ b ^ c, c) + dist(a ^ b ^ c, b)
        # dist(b, c) = dist(a ^ b ^ b, 1 ^ b ^ c) = dist(a, a ^ b ^ c)
        #

        # dist(a1, a2) + dist(a1, a3) ... + dist(a1, an)
        #   =  dist(prefix[n], a1) + dist(prefix[n], a2) ... dist(prefix[n], a_{n - 1})

        #                dist(a2, a3) ... + dist(a2, an)
        #   =  dist(prefix[n], a1) + dist(prefix[n], a2) ... dist(prefix[n], a_{n - 1})

        #                dist(a1, a1 ^ a2 ^ a3)

        #                                   dist(an, an)

        # dist(a1, a2) =>

        def hamming_distance(a, b):
            temp = a ^ b
            return bin(temp)[2:].count("1")

        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                dist = hamming_distance(a, b)
                print(a, b, dist)
                res += dist

        return res
