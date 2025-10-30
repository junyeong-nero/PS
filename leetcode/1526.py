class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        levels = sorted(list(set(target)))
        # print(levels)

        n = len(levels)
        maps = {level: index for index, level in enumerate(levels)}
        maps_r = {index: level for index, level in enumerate(levels)}
        # print(maps)

        target = [maps[elem] for elem in target]
        # print(target)

        boundary = defaultdict(list)
        for i in range(len(target)):
            for j in range(n):
                if target[i] >= j:
                    boundary[j].append(i)

        def continuous_list(arr):
            i = 0
            m = len(arr)
            temp = []
            while i < m:
                j = i
                while j + 1 < m and arr[j] + 1 == arr[j + 1]:
                    j += 1
                temp.append([i, j])
                i = j + 1
            return temp

        for key, value in boundary.items():
            boundary[key] = continuous_list(value)
        # print(boundary)

        weights = [maps_r.get(i, 0) - maps_r.get(i - 1, 0) for i in range(n)]
        # print(weights)

        result = 0
        for i in range(n):
            result += len(boundary[i]) * weights[i]
            
        return result