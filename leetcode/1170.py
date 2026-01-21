class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def f(s):
            smallest_c = min(s)
            return s.count(smallest_c)

        res = []
        n = len(words)
        words = sorted([f(word) for word in words])

        for q in queries:
            index = bisect_right(words, f(q))
            res.append(n - index)

        return res
