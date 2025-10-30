class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        levels = sorted(list(set(target)))
        # print(levels)

        n = len(levels)
        weights = []
        for index, level in enumerate(levels):
            weights.append(levels[index] - levels[index - 1])
            maps[level] = index

        target = [maps[elem] for elem in target]
        boundary = defaultdict(list)
        for i in range(len(target)):
            for j in range(n):
                if target[i] >= j:
                    if j < len(boundary) and boundary[j][-1][1] == i:
                        boundary[j][-1][1] = i + 1
                    else:
                        boundary[j].append([i, i + 1])
        print(boundary)

        # print(weights)

        result = 0
        for i in range(n):
            result += len(boundary[i]) * weights[i]

        return result
