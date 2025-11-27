class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        # 초기 상태
        # s0 -> s1(buy)
        # s0 -> s0(rest)
        # s1 -> s2(sell)
        # s1 -> s1(rest)
        # s2 -> s0(rest)

        s0 = 0
        s1 = -prices[0]
        s2 = float('-inf')
        
        for i in range(1, len(prices)):
            # 임시 변수에 저장하여 동시 업데이트와 유사하게 처리
            prev_s0 = s0
            prev_s1 = s1
            prev_s2 = s2
            
            s0 = max(prev_s0, prev_s2)
            s1 = max(prev_s1, prev_s0 - prices[i])
            s2 = prev_s1 + prices[i]
            
        return max(s0, s2)