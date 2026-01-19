class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        # compare in prefix array

        # [3, 5, 1, 2] -> [0, 3, 8, 9, 11]
        # [4, 6, 2, 4] -> [0, 4, 10, 12, 16]

        # 1. calculate diff = [1, 2, 3, 5]
        # 2. increase [0 ... 3] = 1, then filled with [1, 2, 3, 4]
        # 3. increase [3 ... 3] = 1 then filled with [0, 0, 0, 1]

        # [3, 5, 1, 2] -> [0, 3, 8, 9, 11]
        # [1, 2, 3, 4] -> [0, 1, 3, 6, 10]

        # diff = [-2, -5, -3, -1]
        # 1. decrease [0 ... 1] = 2 , [-1, -2, -2, -2] * 2
        #       [0, -1, 1, 3]
        # 3. decrease [1 ... 3] = 1, [0, -1, -2, 0]
        #       [0, 0, -1, 0]
        # 4. decrease [2 ... 2] = 1 [0, 0, -1, 0]
        #       [0, 0, 0, 0]

        # total = 5

        # [3, 5, 1, 2] -> [4, 6, 2, 4]
        # diff : [1, 1, 1, 3]

        # [3, 5, 1, 2] -> [1, 2, 3, 4]
        # diff : [-2, -3, 1, 2]
        # find index j start from [0 : j]
        # if diff[i] - delta is close to 0, then use it! or break

        # its greedy approach -> failed
        # always minimize abs(first index)
        # but its not optimal...

        def func(diff, index):
            delta = diff[index]
            diff[index] = 0

            j = index + 1
            while j < n:
                if abs(diff[j]) > abs(diff[j] - delta):
                    diff[j] -= delta
                    j += 1
                else:
                    break

            j = index - 1
            while j >= 0:
                if abs(diff[j]) > abs(diff[j] - delta):
                    diff[j] -= delta
                    j -= 1
                else:
                    break

            return diff, abs(delta)

        n = len(nums)
        diff = [target[i] - nums[i] for i in range(n)]
        print(diff)

        res = 0

        indices = sorted(list(range(0, n)), key=abs)

        # O(N)
        for i in indices:
            if diff[i] == 0:
                continue
            diff, count = func(diff, i)
            res += count
            print(diff)

        # need a breakthrought!
        # remove left or remove right?
        # optimal index for removing?

        # [0, 3, -1, -9, 3, 1, 5, 3, 4, 2]

        return res
