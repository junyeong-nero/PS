class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        value = 1
        for _ in range(n):
            res.append(value)
            if value * 10 <= n:
                value *= 10
            else:
                while value % 10 == 9 or value + 1 > n:
                    value //= 10
                value += 1
        return res
    
    # [1]
    # [1, 10]
    # [1, 10, 11, 12, 13]
    # [1, 10, 11, 12, 13, 2]
        