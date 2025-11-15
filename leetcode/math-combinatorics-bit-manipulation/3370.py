class Solution:
    def smallestNumber(self, n: int) -> int:
        for i in range(13):
            temp = 2**i - 1
            if n <= temp:
                return temp
        return -1
