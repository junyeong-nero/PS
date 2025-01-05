class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:    
        text = [(ord(c) - ord('a')) for c in s]
        for info in shifts:
            s, e, d = info
            for i in range(s, e + 1):
                text[i] += (1 if d == 1 else -1)

        return ''.join([chr((c + 26) % 26 + ord('a')) for c in text])