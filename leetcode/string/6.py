class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        d = [[] for _ in range(numRows)]

        direction = -1
        index = 0
        for i, c in enumerate(s):
            d[index].append(c)
            if index % numRows == 0 or index % numRows == numRows - 1:
                direction *= -1
            index += direction

        # print(d)
        return "".join(["".join(row) for row in d])
