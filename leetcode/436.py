class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = list(zip(intervals, range(n)))
        arr = sorted(arr, key=lambda x: x[0][0])
        # print(arr)

        res = []
        for i in range(n):
            end_i = intervals[i][1]
            j = bisect_left(arr, end_i, key=lambda x: x[0][0])
            j = arr[j][1] if j < n else -1
            # print(j)
            res.append(j)

        return res
