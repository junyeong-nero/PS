class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        arr = {}
        counter = Counter()

        res = []
        for query in queries:
            a, b = query[0], query[1]
            if a in arr:
                counter[arr[a]] -= 1
                if counter[arr[a]] == 0:
                    del counter[arr[a]]
            counter[b] += 1
            arr[a] = b

            # print(counter)
            res.append(len(counter.keys()))

        return res
