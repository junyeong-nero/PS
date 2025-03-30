 class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        
        res = 1
        m, n = len(s), len(t)

        for x in range(1, m + 1):
            for y in range(x):
                temp = s[y:x]
                if temp == temp[::-1]:
                    res = max(res, len(temp))
            
        for x in range(1, n + 1):
            for y in range(x):
                temp = t[y:x]
                if temp == temp[::-1]:
                    res = max(res, len(temp))

        i, j = 0, 1
        while i < j and j <= m:
            target = s[i:j][::-1]
            index = t.find(target)
            print(target, index)
            if index != -1:
                parity = 0

                p = index - 1
                while p >= 0:
                    temp = t[p:index]
                    if temp == temp[::-1]:
                        parity = max(parity, len(temp))
                    p -= 1

                p = j + 1
                while p <= m:
                    temp = s[j:p]
                    if temp == temp[::-1]:
                        parity = max(parity, len(temp))
                    p += 1

                print(target, parity)
                res = max(res, (j - i) * 2 + parity)
                j += 1
            else:
                i += 1
                j = i + 1

        return res