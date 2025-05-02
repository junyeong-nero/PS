class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = 'L' + dominoes + 'R'
        result = ""
        left = 0
        for right in range(1, len(dominoes)):
            if dominoes[right] == '.':
                continue
            middle_length = right - left - 1
            if left:
                result += dominoes[left]
            if dominoes[left] == dominoes[right]:
                result += dominoes[left] * middle_length
            elif dominoes[left] == 'L' and dominoes[right] == 'R':
                result += '.' * middle_length
            else:
                result += 'R' * (middle_length // 2) + '.' * (middle_length % 2) + 'L' * (middle_length // 2)
            left = right
        return result