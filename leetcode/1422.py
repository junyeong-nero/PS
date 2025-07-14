class Solution:
    def maxScore(self, s: str) -> int:
        right, left = 0, s.count("1")
        # print(right, left)
        temp = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                right += 1
            if s[i] == "1":
                left -= 1
            temp = max(temp, right + left)

        return temp
