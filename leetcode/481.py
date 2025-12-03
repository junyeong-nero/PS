class Solution:
    def magicalString(self, n: int) -> int:
        arr, i = [1, 2, 2], 2
        while len(arr) < n:
            arr.extend([arr[-1] ^ 3] * arr[i])  # if last number is 1 → next number is 2
            # if last number is 2 → next number is 1
            i += 1
        return arr[:n].count(1)
