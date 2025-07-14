class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for idx, num in enumerate(nums):
            d[num].append(idx)

        res = 0
        for key, value in d.items():
            n = len(value)
            for i in range(n):
                for j in range(i + 1, n):
                    if (value[i] * value[j]) % k == 0:
                        res += 1

        return res
