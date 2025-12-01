class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:

        def next_char(c):
            next_ord = (ord(c) - ord("a") + 1) % 26 + ord("a")
            return chr(next_ord)

        i = 0
        n = len(s)
        d = set()
        while i < n:
            j = i + 1
            while j < n and s[j] == next_char(s[j - 1]):
                j += 1

            temp = s[i:j]
            d.add(s[i:j])
            i = j

        res = set()
        for s in sorted(d, key=len, reverse=True):
            if all([s not in elem for elem in res]):
                res.add(s)

        res = sum([len(s) * (len(s) + 1) // 2 for s in res])
        # res += (j - i) * (j - i + 1) // 2
        # n * (n + 1) // 2
        return res
