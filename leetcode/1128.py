class Solution:
    def numEquivDominoPairs(self, A):
        return sum(
            v * (v - 1) / 2
            for v in collections.Counter(tuple(sorted(x)) for x in A).values()
        )
