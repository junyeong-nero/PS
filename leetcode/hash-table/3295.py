class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:

        bannedWords = set(bannedWords)
        score = [1 if word in bannedWords else 0 for word in message]
        score = sum(score)

        return score >= 2
