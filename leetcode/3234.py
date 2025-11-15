class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        prefix = [0]
        for char in s:
            prefix.append(prefix[-1] + int(char))

        # prefix[i] = sum(s[:i])
        # print(prefix)

        res = 0
        n = len(prefix)
        for i in range(n):
            for j in range(i + 1, n):
                num_ones = prefix[j] - prefix[i]
                num_zeros = j - i - num_ones
                # print(s[i:j], num_zeros, num_ones)
                if num_zeros**2 <= num_ones:
                    res += 1

        return res
