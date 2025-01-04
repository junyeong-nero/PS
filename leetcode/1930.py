from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = defaultdict(list)
        res = 0
        
        for i, c in enumerate(s):
            d[c].append(i)

        for key in d.keys():
            start, end = d[key][0], d[key][-1]
            if start == end:
                continue
            res += len(set(s[start + 1:end]))

        return res