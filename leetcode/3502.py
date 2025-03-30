class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        
        value = float('inf')
        for i in range(len(cost)):
            value = min(value, cost[i])
            cost[i] = value
        
        return cost