import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1. Sort intervals by start time to process them in order
        intervals.sort()

        # 2. Sort queries but keep track of original indices to return answers correctly
        # storing as (query_val, original_index)
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        min_heap = []  # Stores tuple: (size, end_time)
        res = [-1] * len(queries)
        i = 0
        n = len(intervals)

        for q, original_index in sorted_queries:
            # Add all intervals that start before or at the current query
            while i < n and intervals[i][0] <= q:
                start, end = intervals[i]
                size = end - start + 1
                heapq.heappush(min_heap, (size, end))
                i += 1

            # Remove intervals from the heap that end before the current query
            # They are invalid because they don't cover 'q'
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # The top of the heap is now the smallest valid interval covering 'q'
            if min_heap:
                res[original_index] = min_heap[0][0]

        return res


# class Solution:
#     def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

#         n = len(intervals)
#         counter = Counter()
#         maps = dict()

#         events = []
#         for a, b in intervals:
#             size = b - a + 1
#             if size == 1:
#                 maps[a] = 1

#             events.append((a, -size))
#             events.append((b, size))

#         for query in queries:
#             events.append((query, -float("inf")))
#             events.append((query, float("inf")))

#         events = sorted(events)
#         # print(events)

#         for key, size in events:

#             # print(key, size, counter)
#             if size == float("inf") or size == float("-inf"):
#                 temp = min(
#                     [float("inf")]
#                     + [key for key, value in counter.items() if value > 0]
#                 )
#                 maps[key] = min(maps.get(key, float("inf")), temp)
#             elif size < 0:
#                 counter[-size] += 1
#             elif size > 0:
#                 counter[size] -= 1

#         # print(maps)
#         return [-1 if maps[query] == float("inf") else maps[query] for query in queries]
