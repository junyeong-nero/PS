class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:

        walls = [tuple(wall) for wall in walls]
        guards = [tuple(guard) for guard in guards]

        def check_guard(guard):
            x, y = guard
            pos = [1, 0, -1, 0, 1]
            blocks = set()
            for i in range(4):
                dx, dy = pos[i], pos[i + 1]
                tx, ty = x + dx, y + dy

                while 0 <= tx < m and 0 <= ty < n:
                    if (tx, ty) in walls:
                        break
                    if (tx, ty) in guards:
                        break
                    blocks.add((tx, ty))
                    tx, ty = tx + dx, ty + dy

            return blocks

        res = set(walls) | set(guards)
        for guard in guards:
            res |= check_guard(guard)

        return m * n - len(res)
