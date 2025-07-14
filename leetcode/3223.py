class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        for val in counter.values():
            temp = val % 2
            res += 2 if temp == 0 else temp
        return res
