class Solution:
    def solveEquation(self, equation: str) -> str:

        def convert(term):
            if term[0] not in "+-":
                term = "+" + term

            res = [0, 0]
            n = len(term)
            i = 0

            while i < n:

                op = term[i]
                j = i + 1
                while j < n and term[j] not in "+-":
                    j += 1
                temp = term[i + 1 : j]

                check = 0 if "x" in temp else 1
                if temp == "x":
                    temp = 1
                else:
                    temp = int(temp.replace("x", ""))

                if op == "+":
                    res[check] += temp
                else:
                    res[check] -= temp

                i = j

            return res

        right, left = equation.split("=")
        right, left = convert(right), convert(left)
        print(right, left)

        def solve(right, left):

            if right[0] == left[0]:
                if right[1] == left[1]:
                    return "Infinite solutions"
                return "No solution"

            res = (left[1] - right[1]) // (right[0] - left[0])
            return f"x={res}"

        return solve(right, left)
