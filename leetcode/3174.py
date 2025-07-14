class Solution:
    def clearDigits(self, s: str) -> str:
        q = deque([])
        for char in s:
            if char in "0123456789":
                q.pop()
            else:
                q.append(char)

        return "".join(q)
