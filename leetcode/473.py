class Solution:
    def makesquare(self, sticks: List[int]) -> bool:
        value = sum(sticks)
        if value % 4 > 0:
            return False
        length = value // 4
        if max(sticks) > length:
            return False

        print(length)

        n = len(sticks)
        def dfs(index, cur):
            if cur == length:
                return True
            if cur > length:
                return False
            if index >= n:
                return False
            
            if sticks[index] is not None and dfs(index + 1, cur + sticks[index]):
                sticks[index] = None
                return True
            if dfs(index + 1, cur):
                return True
            
            return False
            
        for _ in range(4):
            res = dfs(0, 0)
            print(res, sticks)
            if not res:
                return False
    
        return True
    