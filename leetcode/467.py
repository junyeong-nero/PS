class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        d = defaultdict(int)
        streak = 0
        for i in range(len(p)):
            streak = streak + 1 if (ord(p[i - 1]) - 96) % 26 == (ord(p[i]) - 97) else 1
            d[p[i]] = max(d[p[i]], streak)
        return sum(d.values())
