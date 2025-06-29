class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        counter = Counter(s)
        candidates = [key for key, value in counter.items() if value >= k]
        # print(candidates)

        s = [c for c in s if c in candidates]
        # print(s)
        n = len(s)

        def check(candidate):
            x = len(candidate)
            if x % k != 0:
                return None
            a = x // k
            if candidate[:a] * k == candidate:
                return candidate[:a]
            return None

        seq = ""

        def dfs(index, cur=""):
            if cur:
                temp = check(cur)
                nonlocal seq
                if temp:
                    if len(seq) < len(temp):
                        seq = temp
                    elif len(seq) == len(temp) and temp > seq:
                        seq = temp

            if index >= n:
                return
            dfs(index + 1, cur)
            dfs(index + 1, cur + s[index])

        dfs(0)
        return seq
