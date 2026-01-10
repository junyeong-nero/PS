class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        # dp[i][j]는 s1[i:]와 s2[j:]를 같게 만들기 위한 최소 삭제 비용
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base Case: s1이 빈 문자열일 때 (s2의 나머지를 모두 삭제)
        for j in range(n - 1, -1, -1):
            dp[m][j] = dp[m][j + 1] + ord(s2[j])

        # Base Case: s2가 빈 문자열일 때 (s1의 나머지를 모두 삭제)
        for i in range(m - 1, -1, -1):
            dp[i][n] = dp[i + 1][n] + ord(s1[i])

        # DP Transition
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    # 문자가 같으면 삭제하지 않고 대각선 위로 이동
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # 문자가 다르면 s1[i]를 지우거나, s2[j]를 지우는 것 중 최소값 선택
                    dp[i][j] = min(ord(s1[i]) + dp[i + 1][j], ord(s2[j]) + dp[i][j + 1])

        return dp[0][0]
