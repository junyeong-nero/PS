class Solution:
    def countPairs(self, words: List[str]) -> int:
        n, m = len(words), len(words[0])

        def emb(s):
            first = ord(s[0])
            vector = tuple([(ord(c) - first + 26) % 26 for c in s])
            return vector

        d = Counter([emb(word) for word in words])
        res = sum(value * (value - 1) // 2 for value in d.values())
        return res
