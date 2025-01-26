class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        d = defaultdict(list)
        for i, favor in enumerate(favorite):
            d[favor].append(i)
        print(d)
        # sit beside 2 : [0, 1, 3]
        #      -> 3 * 2 = 6
        #      -> [0, 2, 1] / [0, 2, 3] ... / [3, 2, 1]
        # sit beside 1 : [2]
        # others : no!

        # 2 -> 0 -> 1 -> 2
        # find the longest circular path
        def dfs(cur, visited):
            if visited and cur == visited[0]:
                return 0
            if cur in visited:
                return -1
            temp = -1
            for elem in d[cur]:
                temp = max(temp, dfs(elem, visited + [cur]))
            return temp + 1

        res = 0
        for i in range(n):
            res = max(res, dfs(i, []))
        return res