from typing import List

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start = [(start[i], i) for i in range(n) if start[i] != '_']
        target = [(target[i], i) for i in range(n) if target[i] != '_']
    
        if len(start) != len(target):
            return False
            
        return all([
            start[i][0] == target[i][0] and (
                (start[i][0] == 'L' and start[i][1] >= target[i][1]) or 
                (start[i][0] == 'R' and start[i][1] <= target[i][1])
            )
            for i in range(len(start))
        ])
        
        
res = Solution().canChange('_L__R__R_', 'L______RR')
print(res)