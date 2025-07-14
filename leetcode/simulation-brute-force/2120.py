class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        dirs = {"U": (-1, 0), "D": (+1, 0), "R": (0, +1), "L": (0, -1)}

        def func(cur, query):
            count = 0
            x, y = cur
            for move in query:
                dx, dy = dirs[move]
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                count += 1
                x, y = nx, ny

            return count

        res = []
        for i in range(len(s)):
            res.append(func(startPos, s[i:]))

        return res
