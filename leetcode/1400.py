from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        counter = Counter(s)
        odd_count = sum(1 for v in counter.values() if v % 2 == 1)
        return odd_count <= k