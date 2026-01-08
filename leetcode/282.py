class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        n = len(num)

        def calculate(eq):
            eq = eq.replace("-", "+-")
            arr = eq.split("+")

            def func(s):
                res = 1
                for elem in s.split("*"):
                    res *= int(elem)
                return res

            res = 0
            for eq in arr:
                res += func(eq)

            return res

        # for each steps with addings +, *, - operations, numbers are decreased.
        # - 1234 > 1 + 234 = 235
        # - 1234 > 1 * 234 = 234

        # Break if calculated numbers < target
        # add operations randomly

        def dfs(index, equation):
            if index == n:
                if calculate(equation) == target:
                    return [equation]
                return []
            # if calculate(equation) > target:
            #     return []

            res = []
            res += dfs(index + 1, equation + "*" + num[index])
            res += dfs(index + 1, equation + "+" + num[index])
            res += dfs(index + 1, equation + "-" + num[index])
            if equation[-1] != "0":
                res += dfs(index + 1, equation + num[index])

            return res

        res = dfs(1, num[0])
        return res
