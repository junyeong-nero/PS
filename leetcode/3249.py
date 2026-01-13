class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:

        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        res = 0

        def subtree(cur, prev):
            count = []
            for node in tree[cur]:
                if node == prev:
                    continue
                count.append(subtree(node, cur))

            # print(cur, count)
            if not count or len(set(count)) == 1:
                nonlocal res
                res += 1

            return sum(count) + 1

        subtree(0, -1)
        return res
