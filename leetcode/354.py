class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        # 1. 가로 길이 기준 오름차순 정렬
        envelopes.sort()
        n = len(envelopes)

        # 2. dp[i]: i번째 봉투를 가장 바깥으로 했을 때 최대 개수
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                # i번째 봉투가 j번째 봉투를 담을 수 있는지 확인
                if (
                    envelopes[j][0] < envelopes[i][0]
                    and envelopes[j][1] < envelopes[i][1]
                ):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
