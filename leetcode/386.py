class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        if n < 10:
            return list(range(1, n + 1))
        
        @cache
        def dfs(num):
            if num > n:
                return []

            temp = []
            for i in range(10):
                if num == 0 and i == 0:
                    continue
                temp += dfs(num * 10 + i)
            
            return [num] + temp

        return dfs(0)[1:]