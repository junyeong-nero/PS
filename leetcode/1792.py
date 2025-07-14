from heapq import heappush, heappop, heapify


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        classes = [
            (tar[0] / tar[1] - (tar[0] + 1) / (tar[1] + 1), tar[0], tar[1])
            for tar in classes
        ]
        heapify(classes)

        for _ in range(extraStudents):
            _, a, b = heappop(classes)
            a, b = (
                a + 1,
                b + 1,
            )
            grad = a / b - (a + 1) / (b + 1)
            heappush(classes, (grad, a, b))

        return sum([x[1] / x[2] for x in classes]) / n
