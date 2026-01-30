from collections import Counter
from typing import List

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        """
        [핵심 아이디어]
        1. 'Beautiful Subarray'란 모든 비트의 개수가 짝수인 배열입니다.
        2. xor 연산 시 같은 숫자를 짝수 번 연산하면 0이 됩니다.
        3. 따라서 특정 구간 [i, j]의 xor 합이 0이면, 해당 구간은 beautiful subarray입니다.
        4. Prefix XOR(누적 XOR)의 성질을 이용합니다:
           - subarray(i...j)의 XOR 합 = prefix_xor(j) ^ prefix_xor(i-1)
           - 이 값이 0이 되려면 prefix_xor(j) == prefix_xor(i-1)이어야 합니다.
        """
        
        # dp[val]: 지금까지 나타난 prefix xor 값 'val'의 빈도수
        # {0: 1} 초기화 이유: 맨 처음부터 현재까지의 xor 합이 0인 경우를 카운트하기 위함
        dp = Counter({0: 1})
        
        res = 0    # 총 beautiful subarray 개수
        pre = 0    # 현재 인덱스까지의 누적 xor 합 (Prefix XOR)
        
        for num in nums:
            # 1. 현재 숫자까지의 누적 XOR 합 업데이트
            pre ^= num
            
            # 2. 이전에 동일한 누적 XOR 값이 나타났는지 확인
            # 만약 이전에 동일한 pre가 있었다면, 그 지점 이후부터 현재까지의 XOR 합은 0임
            res += dp[pre]
            
            # 3. 현재의 누적 XOR 값을 카운터에 기록
            dp[pre] += 1

        return res
