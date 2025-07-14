class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:

        arr = [
            (1 if i == firstPlayer or i == secondPlayer else 0) for i in range(1, n + 1)
        ]

        def turns(arr, history, index=0):
            n = len(arr)
            index_r = n - 1 - index
            if index >= index_r:
                history = [elem for elem in history if elem != -1]
                return [tuple(history)]

            res = []
            if arr[index] == 1 and arr[index_r] == 1:
                return [None]

            if arr[index] == 1:
                history[index_r] = -1
                return turns(arr, history, index + 1)

            if arr[index_r] == 1:
                history[index] = -1
                return turns(arr, history, index + 1)

            history[index] = -1
            temp = turns(arr, history, index + 1)
            if temp:
                res += temp
            history[index] = 0

            history[index_r] = -1
            temp = turns(arr, history, index + 1)
            if temp:
                res += temp
            history[index_r] = 0

            return res

        q = deque([arr])
        level = 1
        min_level = float("inf")
        max_level = -1

        while q:
            # print(q)
            q_next = []

            for _ in range(len(q)):
                tar = q.popleft()
                temp = turns(tar, tar[:])
                for elem in temp:
                    if elem is not None:
                        continue
                    min_level = min(min_level, level)
                    max_level = max(max_level, level)

                q_next += temp

            q_next = list(set(q_next))
            q_next = [list(elem) for elem in q_next if elem]
            q.extend(q_next)

            level += 1

        # print(min_level, max_level)
        return [min_level, max_level]
