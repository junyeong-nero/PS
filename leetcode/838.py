class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        prefix_right = [0]
        prefix_left = [0]

        num = 0
        for domino in dominoes:
            if domino == "L":
                num = 0
            elif domino == "R":
                num += 1
            elif domino == "." and num > 0:
                num += 1
            prefix_right.append(num)

        prefix_right = prefix_right[1:]

        num = 0
        for domino in dominoes[::-1]:
            if domino == "R":
                num = 0
            elif domino == "L":
                num += 1
            elif domino == "." and num > 0:
                num += 1
            prefix_left.append(num)

        prefix_left = prefix_left[1:][::-1]

        print(prefix_right)
        print(prefix_left)

        n = len(prefix_right)

        res = ""
        for i in range(n):
            diff = prefix_right[i] - prefix_left[i]
            if diff > 0:
                res += "R"
            if diff < 0:
                res += "L"
            if diff == 0:
                res += "."

        return res
