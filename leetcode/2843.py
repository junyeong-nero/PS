class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for num in range(low, high + 1):
            temp = list(map(int, str(num)))
            # print(temp)
            n = len(temp)
            if n % 2 == 1:
                continue
            if sum(temp[: n // 2]) == sum(temp[n // 2 :]):
                res += 1

        return res
