class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(s):
            hour, minute = s.split(":")
            return 60 * int(hour) + int(minute)

        times = sorted([convert(time) for time in timePoints])
        n = len(times)
        res = float("inf")
        
        times.append(24 * 60 + times[0])
        for i in range(n):
            a, b = times[i], times[i + 1]
            res = min(res, b - a)

        return res