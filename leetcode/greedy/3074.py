class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        prefix = [0]
        capacity = sorted(capacity, reverse=True)
        for cap in capacity:
            prefix.append(prefix[-1] + cap)

        i = bisect_left(prefix, sum(apple))
        return i
