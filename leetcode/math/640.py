import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        # Split equation into Left Hand Side (lhs) and Right Hand Side (rhs)
        lhs, rhs = equation.split("=")

        def evaluate(expression: str) -> tuple[int, int]:
            """Parses the expression and returns (coefficient_of_x, constant_sum)."""
            tokens = re.findall(r"[+-]?\d*x?", expression)
            x_coeff = 0
            constant_sum = 0

            for token in tokens:
                if not token:
                    continue  # Skip empty matches caused by regex

                if "x" in token:
                    # Handle cases like "x", "-x", "+x", "2x", "-3x"
                    if token == "x" or token == "+x":
                        val = 1
                    elif token == "-x":
                        val = -1
                    else:
                        val = int(token.replace("x", ""))
                    x_coeff += val
                else:
                    # Handle constants like "5", "-3", "+2"
                    constant_sum += int(token)

            return x_coeff, constant_sum

        # Calculate coefficients for both sides
        l_x, l_const = evaluate(lhs)
        r_x, r_const = evaluate(rhs)

        # Simplify to form: ax = b
        # a = l_x - r_x
        # b = r_const - l_const
        a = l_x - r_x
        b = r_const - l_const

        # Check for edge cases
        if a == 0:
            if b == 0:
                return "Infinite solutions"
            else:
                return "No solution"

        return f"x={b // a}"
