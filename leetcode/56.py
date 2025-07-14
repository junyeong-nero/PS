class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        n = len(intervals)

        arr = []
        i = 0
        while i < n:
            j = i
            temp = intervals[i][1]
            while j + 1 < n:
                if intervals[j + 1][0] <= temp:
                    temp = max(temp, intervals[j + 1][1])
                    j += 1
                else:
                    break

            arr.append([intervals[i][0], temp])
            i = j + 1

        return arr
