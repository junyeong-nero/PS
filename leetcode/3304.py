class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            temp = ""
            for char in word:
                if char == "z":
                    temp += "a"
                else:
                    temp += chr(ord(char) + 1)
            word = word + temp
        return word[k - 1]