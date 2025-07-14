class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            p, b = questions[i]
            nextQuestion = min(n, i + b + 1)
            dp[i] = max(dp[i + 1], p + dp[nextQuestion])

        return dp[0]
