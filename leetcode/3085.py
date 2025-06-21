class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        arr = sorted(list(counter.values()))
        # print(arr)

        n = len(arr)
        res = float('inf')

        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        i, j = 0, 0
        for i in range(n):
            for j in range(i, n):
                diff = arr[j] - arr[i]
                if diff <= k:
                    temp = prefix[i] + sum([max(0, arr[index] - (arr[i] + k)) for index in range(j + 1, n)])
                    res = min(res, temp)
            
        return res if res != float('inf') else 0