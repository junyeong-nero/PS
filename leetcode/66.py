class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        last = 1
        res = []
        for digit in digits:
            digit += last
            if digit == 10:
                digit = 0
                last = 1
            else:
                last = 0
            res.append(digit)

        if last > 0:
            res.append(last)

        return res[::-1]
