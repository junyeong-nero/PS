class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        prefix = [Counter()]
        for char in s:
            prefix.append(prefix[-1] + Counter(char))
        # print(prefix)

        def check(counter):
            common = counter.most_common()
            # print(common)
            if len(common) <= 1:
                return sum([value for key, value in common])

            out = 0
            for key, value in common[1:]:
                out += value

            if out > k:
                return -1
            return sum([value for key, value in common])

        res = float("-inf")
        for i in range(1, n + 1):
            for j in range(i):
                counter = prefix[i] - prefix[j]
                temp = check(counter)
                if temp > 0:
                    res = max(res, temp)
                    break

        return res
