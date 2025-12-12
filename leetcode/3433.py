class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:

        online = [True] * n
        future_online = defaultdict(list)

        events = sorted(
            events, key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1)
        )
        print(events)

        def get_id(s):
            if s == "HERE":
                return [i for i in range(n) if online[i]]
            if s == "ALL":
                return list(range(n))

            arr = s.split()
            return [
                int(elem.replace("id", ""))
                for elem in arr
                if "id" in elem or elem.isnumeric()
            ]

        res = [0] * n

        for event in events:
            event_type, timestamp, ids = event
            timestamp = int(timestamp)
            for time in future_online:
                if time > timestamp:
                    continue
                for _id in future_online[time]:
                    online[_id] = True
                future_online[time].clear()

            ids = get_id(ids)

            if event_type == "MESSAGE":
                for _id in ids:
                    res[_id] += 1

            if event_type == "OFFLINE":
                for _id in ids:
                    online[_id] = False
                    future_online[timestamp + 60].append(_id)

        return res
