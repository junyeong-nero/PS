class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sort = sorted(nums)
        res = []

        @cache
        def dfs(index):
            if index == n:
                return True

            temp = False
            for i in range(n):
                if sort[i] == -1 or abs(sort[i] - nums[index]) > limit:
                    continue
                
                origin = sort[i]
                sort[i] = -1
                if dfs(index + 1):
                    temp = True
                    res.append(origin)
                    break
                sort[i] = origin
            return temp

        dfs(0)
        return res[::-1]