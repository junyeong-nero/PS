class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        d = defaultdict(list)

        def get_base(num):
            while num % 2 == 0 and num > 0:
                num //= 2
            return num

        def func(arr, base):
            res = 0
            left, right = Counter(), Counter(arr)
            for num in arr:
                left[num] += 1
                right[num] -= 1
                res += left[num * 2] * right[num * 2]
            return res % MOD

        for num in nums:
            base = get_base(num)
            d[base].append(num)

        # print(d)

        res = 0
        if len(d[0]) >= 3:
            t = len(d[0])
            res += t * (t - 1) * (t - 2) // 6  # n C 3
            res %= MOD

        for base, arr in d.items():
            if base == 0:
                continue
            res += func(arr, base)
            res %= MOD

        return res
