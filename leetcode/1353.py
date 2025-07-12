class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        events.sort(key=lambda x: x[1])
        res = 0

        last_day = 0
        for event in events:
            if event[1] >= last_day:
                res += 1
                last_day = max(last_day, event[0]) + 1

        return res

        # [1, 2]
        # [2, 3]
        # [5, 10]
