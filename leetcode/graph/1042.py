class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        # for u, v in paths, answer[u] != answer[v]
        # O(n^2) solution
        graph = defaultdict(list)
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)

        colors = [-1] * n

        def get_color(node):
            no_colors = set()
            for neighbor in graph[node]:
                no_colors.add(colors[neighbor - 1])

            return {1, 2, 3, 4} - no_colors

        for i in range(n):
            colors[i] = get_color(i + 1).pop()

        return colors
