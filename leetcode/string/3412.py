class Solution:
    def calculateScore(self, s: str) -> int:

        def mirror(c):
            index = ord(c) - ord("a")
            return chr(25 - index + ord("a"))

        # print(s)
        # print("".join([mirror(c) for c in s]))

        d = defaultdict(deque)
        res = 0
        for i, c in enumerate(s):
            c_mirror = mirror(c)
            if d[c_mirror] and (j := d[c_mirror][-1]) < i:
                d[c_mirror].pop()
                res += i - j
                # print(i, j)
            else:
                d[c].append(i)

        return res
