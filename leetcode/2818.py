class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        def prime_score(num):
            i = 2
            primes = set()
            while num > 1:
                while num % i == 0:
                    num /= i
                    primes.add(i)
                i += 1
            return len(primes)

        # print(prime_score(300))

        heap = []
        for idx, num in enumerate(nums):
            score = prime_score(num)
            heappush(heap, (-score, -num, idx))

        MOD = 10 ** 9 + 7
        # [0, 1, 2, 3] * [3, 4, 5]

        res = 1
        while k > 0:
            score, num, idx = heappop(heap)
            count = min(k, (idx + 1) * (n - idx))
            print(-score, -num, idx, count)

            res = res * (-num) ** count
            res = res % MOD
            k -= count
            
        return res