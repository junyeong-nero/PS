class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        # for square, there are same number of continuous removable bars in hBars and vBars
        # for example, n = 2, m = 3 and hBars = [2, 3], vBars = [3, 4]
        # then answer = 9 (3 * 3)
        # => need to calculate the length of continuous array

        hBars, vBars = sorted(hBars), sorted(vBars)

        def func(arr):
            n = len(arr)
            i = 0
            res = []
            while i < n:
                j = i + 1
                while j < n and arr[j] - arr[j - 1] == 1:
                    j += 1

                res.append(j - i)
                i = j
            return res

        h, v = func(hBars), func(vBars)
        # print(h, v)

        res = min(max(h), max(v))
        # print(res)

        res = (res + 1) ** 2
        return res
