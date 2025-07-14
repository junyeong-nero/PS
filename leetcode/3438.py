class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)
        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            if a == b:
                continue
            if a == str(counter[a]) and b == str(counter[b]):
                return a + b

        return ""
