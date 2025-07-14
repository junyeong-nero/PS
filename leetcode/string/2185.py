class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(
            [
                1
                for word in words
                if len(word) >= len(pref) and word[: len(pref)] == pref
            ]
        )
