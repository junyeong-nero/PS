class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        
        n = len(s)

        def diff(info):
            arr = list(info.values())
            if sum(arr) < k:
                return -float('inf')

            _min, _max = float('inf'), -1
            for num in arr:
                if num <= 0:
                    continue
                if num % 2 == 1:
                    _max = max(_max, num)
                else:
                    _min = min(_min, num)

            if _min == float('inf') or _max == -1:
                return -float('inf')
            return _max - _min 
        
        def dfs(index, info):

            temp = diff(info)
            if index >= len(s):
                return temp
                
            temp = max(temp, dfs(index + 1, info))
            info[s[index]] += 1
            temp = max(temp, dfs(index + 1, info))
            info[s[index]] -= 1

            return temp
            
    
        res = dfs(0, {s:0 for s in "01234"})
        return res

        

