class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        i = 0
        res = 1
        while i < n:
            j = i
            while j < n and word[i] == word[j]:
                j += 1
            res += j - i - 1
            i = j

        return res
