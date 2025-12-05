class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1

        n = len(a)
        m = len(b)
        count = b.count(a)
        if count == 0:
            for i in range(m):
                temp = a[-1 - i :] + a[: m - i - 1]
                if temp == b:
                    return 2
            return -1

        res = count
        b = "[" + b + "]"
        arr = [elem for elem in b.split(a) if elem and elem != "[" and elem != "]"]
        # print(arr)
        if len(arr) > 2:
            return -1

        def check(target, direct):
            for i in range(n):
                temp = a[i:] if direct else a[:i]
                if temp == target:
                    return True
            return False

        if len(arr) == 1:
            target = arr[0]
            direct = True if target[0] == "[" else False
            target = target[1:] if direct else target[:-1]
            if check(target, direct):
                return res + 1
            return -1

        if len(arr) == 2:
            target_left = arr[0][1:]
            target_right = arr[1][:-1]
            if check(target_left, True) and check(target_right, False):
                return res + 2
            return -1

        return res
