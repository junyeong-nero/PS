from heapq import heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        arr = []
        for i in range(n):
            tar = classes[i]
            grad = (tar[0] + 1) / (tar[1] + 1) - tar[0] / tar[1]
            heappush(arr, (-grad, tar[0], tar[1]))

        for _ in range(extraStudents):
            tar = heappop(arr)
            grad = (tar[1] + 2) / (tar[2] + 2) - (tar[1] + 1) / (tar[2] + 1)
            heappush(arr, (-grad, tar[1] + 1, tar[2] + 1))

        return sum([x[1] / x[2] for x in arr]) / n