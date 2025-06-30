class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter()
        for num in nums:
            counter[num] += 1
        # print(counter)

        res = 0
        for key in counter.keys():
            a = counter[key]
            b = counter[key + 1]
            if a == 0 or b == 0:
                continue
            res = max(res, a + b)

        return res
