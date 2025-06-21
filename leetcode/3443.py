class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        counter = Counter(s)
        n, s, e, w = counter["N"], counter["S"], counter["E"], counter["W"]
        if n < s:
            n, s = s, n
        if e < w:
            e, w = w, e
        
        # n > s
        # e > w
        return n + e + min(s + w, k) * 2