class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        prefix = [0]
        for char in s:
            prefix.append(prefix[-1] + int(char))

        # prefix[i] = sum(s[:i])
        print(prefix)

        res = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                num_ones = prefix[j] - prefix[i]
                num_zeros = j - i - num_ones
                print(s[i:j], num_ones, num_zeros)
                if num_zeros**2 <= num_ones:
                    res += 1

        return res
