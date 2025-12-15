class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0
        res = 0
        while i < n:
            j = i + 1
            while j < n and prices[j] == prices[j - 1] - 1:
                j += 1
            # print(j - i)
            res += (j - i) * (j - i + 1) // 2 
            i = j
        
        return res