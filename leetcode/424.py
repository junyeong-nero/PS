class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        def check(counter):
            common = counter.most_common()
            if len(common) <= 1:
                return sum([0] + [value for key, value in common])

            out = sum([value for key, value in common[1:]])
            if out > k:
                return -1
            return sum([value for key, value in common])

        i = 0
        j = 0
        res = 0
        counter = Counter()
        while i <= j and j < n:
            if (temp := check(counter)) >= 0:
                counter[s[j]] += 1
                j += 1
                res = max(res, temp)
            else:
                counter[s[i]] -= 1
                i += 1

        res = max(res, check(counter))
        return res
