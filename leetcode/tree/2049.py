class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        n = len(parents)
        graph = defaultdict(list)
        for node, parent in enumerate(parents):
            if parent == -1:
                continue
            graph[parent].append(node)
            graph[node].append(parent)

        # print(graph)

        @cache
        def size(node, prev=-1):
            return 1 + sum(
                [size(neigh, node) for neigh in graph[node] if neigh != prev]
            )

        @cache
        def score(node):
            arr = []
            for neigh in graph[node]:
                temp = size(neigh, node)
                arr.append(temp)

            # print(node, arr)
            res = 1
            for num in arr:
                res *= num
            return res

        counter = Counter()
        for i in range(n):
            temp = score(i)
            counter[temp] += 1

        # print(counter)
        return counter[max(counter.keys())]


# class Solution:
#     def countHighestScoreNodes(self, parents: List[int]) -> int:
#         n = len(parents)
#         children = [[] for _ in range(n)]

#         for i in range(1, n):
#             children[parents[i]].append(i)

#         max_score = 0
#         count = 0

#         def dfs(node):
#             nonlocal max_score, count

#             size = 1
#             score = 1

#             for child in children[node]:
#                 child_size = dfs(child)
#                 size += child_size
#                 score *= child_size

#             remaining = n - size
#             if remaining > 0:
#                 score *= remaining

#             if score > max_score:
#                 max_score = score
#                 count = 1
#             elif score == max_score:
#                 count += 1

#             return size

#         dfs(0)
#         return count
