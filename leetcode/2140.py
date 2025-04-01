class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        dp = dict()

        @cache
        def func(cur):
            if cur in dp:
                return dp[cur]
            if cur >= n:
                return 0
                
            res = 0
            for i in range(cur, n):
                point, brain = questions[i]
                res = max(res, point + func(i + brain + 1))

            dp[cur] = res
            return res

        return func(0)
