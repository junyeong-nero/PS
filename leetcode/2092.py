class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
                return rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
                return rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
                return rootX

        return rootX


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:

        graph = defaultdict(list)
        uf = UnionFind(n)

        def concatenate(arr):
            uf.__init__(n)
            roots = defaultdict(set)
            for u, v in arr:
                if uf.find(u) == uf.find(v):
                    continue

                root = uf.union(u, v)
                roots[root] |= {u, v}
            return list(roots.values())

        for u, v, time in meetings:
            graph[time].append([u, v])

        for time in graph:
            graph[time] = concatenate(graph[time])

        times = sorted(graph.keys())
        # print(graph)
        # print(times)

        secret = [False] * n
        secret[0] = True
        secret[firstPerson] = True

        for time in times:
            for group in graph[time]:
                know_secret = any([secret[i] for i in group])
                if not know_secret:
                    continue
                for i in group:
                    secret[i] = True

        res = [i for i in range(n) if secret[i]]
        return res
