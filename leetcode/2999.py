class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        n = len(s)
        a, b = str(start), str(finish)

        def func(x):
            temp = int(x)
            return temp
            # return temp if temp <= limit else limit

        start_t = [0]
        if len(a) > 2:
            start_t = list(map(func, a[:-n]))
        finish_t = list(map(func, b[:-n]))

        def order(arr, base):
            res = 0
            temp = 1
            carry = 0
            for num in arr[::-1]:
                if carry + num >= base:
                    carry = 1
                    num = 0
                else:
                    carry = 0

                res += temp * num
                temp *= base
            if carry == 1:
                res += temp
            return res

        print(start_t, finish_t)
        a = order(finish_t, limit + 1)
        b = order(start_t, limit + 1)
        print(a, b)

        return a - b