class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        MOD = 10 ** 9 + 7

        def prime_score(num):
            score = 0
            i = 2
            while i * i <= num:
                if num % i == 0:
                    score += 1
                    while num % i == 0:
                        num //= i
                i += 1
            if num > 1:
                score += 1
            return score

        d = {x: prime_score(x) for x in set(nums)} 
        scores = [d[x] for x in nums]
        arr = sorted([(num, idx) for idx, num in enumerate(nums)], reverse=True)

        # print(scores)
        # print(arr)

        res = 1
        i = 0

        while k > 0:
            if i >= n:
                break
            num, index = arr[i]

            x = y = index
            while x - 1 >= 0 and scores[x - 1] < scores[index]:
                x -= 1
            while y + 1 < n and scores[y + 1] <= scores[index]:
                y += 1

            count = min(k, (index - x + 1) * (y - index + 1))
            res = (res * num ** count) % MOD

            i += 1
            k -= count

        return res