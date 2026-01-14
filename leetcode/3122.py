class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        columns = [[grid[i][j] for i in range(m)] for j in range(n)]
        columns_counter = [Counter(column) for column in columns]

        def check_row(row):
            prev, prev_idx = -1, 0
            errors = []
            for idx, elem in enumerate(row):
                if elem == prev:
                    if not errors or errors[-1] != prev_idx:
                        errors.append(prev_idx)
                    errors.append(idx)
                prev, prev_idx = elem, idx

            # 011011

            return check_cost(row, check_error_count(errors))

        def check_error_count(errors):
            i = 0
            res = 0
            print(errors)
            while i < len(errors):
                j = i
                while j + 1 < len(errors) and errors[j + 1] - errors[j] == 1:
                    j += 1
                res += (j - i + 1) // 2
                i = j + 1
            return res

        def func(column_counter, target):
            for key, freq in column_counter.most_common():
                if key == target:
                    continue
                return freq
            return 0

        def check_cost(row, errors=0):
            print(row, errors)
            res = []
            for i in range(n):
                value = row[i]
                res.append((columns_counter[i][value], func(columns_counter[i], value)))
                # columns_counter[i]

            res = sorted(res, key=lambda x: x[0] - x[1])
            print(res)
            # errors * m -> column 을 모두 바꾸는게 아니라
            # most frequency elements 기준으로 바꿔야 한다.
            return (
                m * n
                - sum([elem[0] for elem in res[errors:]])
                - sum([elem[1] for elem in res[:errors]])
            )

        temp = [check_row(row) for row in grid]
        print(temp)

        return min(temp)
