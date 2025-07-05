class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        def func(word):
            res = ""
            for char in word:
                res += "a" if char == "z" else chr(ord(char) + 1)
            return res

        word = "a"
        for op in operations:
            if op == 0:
                word = word + word
            if op == 1:
                word = word + func(word)

            if len(word) >= k:
                break

        return word[k - 1]
