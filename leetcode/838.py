class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        arr = [0] * n

        i = 0
        while i < n:
            if dominoes[i] == "R":
                j = i
                while j < n and dominoes[j] != "L":
                    arr[j] += 1
                    j += 1
                i = j
            else:
                i += 1
        print(arr)

        i = n - 1
        while i >= 0:
            if dominoes[i] == "L":
                j = i
                while j >= 0 and dominoes[j] != "R":
                    arr[j] -= 1
                    j -= 1
                i = j
            else:
                i -= 1

        print(arr)

        res = ""
        for num in arr:
            if num > 0:
                res += "R"
            if num == 0:
                res += "."
            if num < 0:
                res += "L"

        return res
