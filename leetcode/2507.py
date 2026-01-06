class Solution:
    def smallestValue(self, n: int) -> int:

        def func(num):
            cur = 2
            arr = []
            while cur <= num:
                if num % cur == 0:
                    num //= cur
                    arr.append(cur)
                    cur -= 1
                cur += 1

            return sum(arr)

        prev, cur = None, n
        while prev != cur:
            prev, cur = cur, func(cur)

        return cur
