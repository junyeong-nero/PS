class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        MOD = 10 ** 9 + 7

        def prime_score(num):
            i = 2
            primes = set()
            while num > 1:
                while num % i == 0:
                    num /= i
                    primes.add(i)
                i += 1
            return len(primes)

        scores = [prime_score(x) for x in nums]
        arr = sorted([(num, idx) for idx, num in enumerate(nums)], reverse=True)

        # print(scores)
        # print(arr)

        res = 1
        i = 0

        while k > 0:
            if i >= n:
                break
            num, index = arr[i]

            x = index
            y = index
            while x - 1 >= 0 and scores[x - 1] < scores[index]:
                x -= 1
            while y + 1 < n and scores[y + 1] <= scores[index]:
                y += 1

            # scores[index] = float('inf')
            count = min(k, (index - x + 1) * (y - index + 1))
            # print(num, count)
            res = (res * num ** count) % MOD

            i += 1
            k -= count


        return res