class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        prefix = [0]
        for num in differences:
            prefix.append(prefix[-1] + num)

        a, b = lower - min(prefix), upper - max(prefix)
        return max(0, b - a + 1)
