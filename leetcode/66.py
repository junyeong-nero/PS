class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(digit) for digit in digits])) + 1
        return [int(digit) for digit in list(str(num))]
