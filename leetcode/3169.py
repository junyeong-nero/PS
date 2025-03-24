class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)
        # print(meetings)

        last_day = 0
        result = 0 
        for meeting in meetings:
            start, end = meeting
            result += max(0, start - last_day - 1)
            last_day = max(last_day, end)

        result += max(0, days - last_day)
        return result