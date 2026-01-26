class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        n = len(arr)
        arr = sorted(arr)
        d = defaultdict(list)
        for i in range(n - 1):
            value = abs(arr[i + 1] - arr[i])
            d[value].append([arr[i], arr[i + 1]])

        key = min(d.keys())
        return d[key]
