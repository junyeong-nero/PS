class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Convert number to a list of characters for easy modification
        digits = list(str(n))
        size = len(digits)

        # 'marker' tracks where we should start filling with 9s
        marker = size

        # Iterate from right to left
        for i in range(size - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                marker = i
                # Decrease the current digit by 1
                digits[i - 1] = str(int(digits[i - 1]) - 1)

        # All digits from the marker to the end become 9
        for i in range(marker, size):
            digits[i] = "9"

        return int("".join(digits))
