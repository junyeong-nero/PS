class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)

        boundary = [(value[0], value[-1]) for key, value in d.items()]
        boundary = sorted(boundary)

        cur = [0, -1]
        res = []
        for bound in boundary:
            if cur[1] >= bound[0]:
                cur[1] = max(cur[1], bound[1])
            else:
                if cur[1] >= 0:
                    res.append(cur)
                cur = [bound[0], bound[1]]

        res.append(cur)
        return [elem[1] - elem[0] + 1 for elem in res]
