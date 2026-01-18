class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        # already deleted some fences.
        # calculate continuous fences

        MOD = 10**9 + 7

        def func(arr):
            arr = sorted(arr)
            diff = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
            return diff

        h_arr, v_arr = func([1] + hFences + [m]), func([1] + vFences + [n])
        # print(h_arr, v_arr)

        prefix_h, prefix_v = [0], [0]
        for num in h_arr:
            prefix_h.append(prefix_h[-1] + num)
        for num in v_arr:
            prefix_v.append(prefix_v[-1] + num)

        res = float("-inf")

        # constraint -> solve in O(N ** 2)
        h_set = set()
        for i in range(1, len(prefix_h)):
            for j in range(i):
                h_set.add(prefix_h[i] - prefix_h[j])

        v_set = set()
        for i in range(1, len(prefix_v)):
            for j in range(i):
                v_set.add(prefix_v[i] - prefix_v[j])

        # print(h_set, v_set)
        intersect = set(h_set) & set(v_set)
        if intersect:
            temp = max(intersect)
            res = max(res, temp**2 % MOD)

        return -1 if res == float("-inf") else res
