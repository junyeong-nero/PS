class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        res = 0 # [1, n]

        def func(index, his):
            arr = [nums[i] for i in his]
            if his and (max(arr) - min(arr)) > k:
                return []
            if index >= n:
                return his

            res = his[:]
            temp = func(index + 1, his)
            if len(temp) > len(res):
                res = temp

            # select
            if nums[index] != -1:
                temp = func(index + 1, his + [index])
                if len(temp) > len(res):
                    res = temp

            return res


        total = 0
        while total < n:
            used = func(0, [])
            # print(used)
            # print(nums)
            for i in used:
                nums[i] = -1
            total += len(used)
            res += 1

        return res