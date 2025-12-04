class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        stack = deque()

        res = 0
        for i in range(n):
            if directions[i] == "R":
                stack.append("R")
            elif directions[i] == "L":
                if stack and stack[-1] == "R":
                    while stack and stack[-1] == "R":
                        stack.pop()
                        res += 1
                    res += 1
                    stack.append("S")
                elif stack and stack[-1] == "S":
                    res += 1
                    stack.append("S")
                else:
                    stack.append("L")
            elif directions[i] == "S":
                if stack and stack[-1] == "R":
                    while stack and stack[-1] == "R":
                        stack.pop()
                        res += 1
                stack.append("S")
            # print(i, stack)

        return res
