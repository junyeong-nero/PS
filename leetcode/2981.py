from itertools import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(list)
        text, size = "", 0

        for i in range(len(s)):
            if text == s[i]:
                size += 1
            else:
                text = s[i]
                size = 1
            d[text].append(size)

        arr = [sorted(x, reverse=True)[2] for x in d.values() if len(x) >= 3]
        return max(arr) if arr else -1
