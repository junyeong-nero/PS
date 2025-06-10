class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        # print(counter)

        a = max([value for value in counter.values() if value % 2 == 1])
        b = min([value for value in counter.values() if value % 2 == 0])
        return a - b