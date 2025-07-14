class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words = set(words)
        for word in words:
            if any([word in temp for temp in words if word != temp]):
                res.append(word)

        return res
