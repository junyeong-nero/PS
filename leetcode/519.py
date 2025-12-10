class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.zeros = set()

    def flip(self) -> List[int]:
        x, y = random.randint(0, self.m - 1), random.randint(0, self.n - 1)
        while (x, y) in self.zeros:
            x, y = random.randint(0, self.m - 1), random.randint(0, self.n - 1)

        self.zeros.add((x, y))
        return x, y

    def reset(self) -> None:
        self.zeros = set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
