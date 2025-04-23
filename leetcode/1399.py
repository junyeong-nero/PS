class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        d = Counter()
        for i in range(1, n + 1):
            digit_sum = sum(list(map(int, list(str(i)))))
            d[digit_sum] += 1

        j = max(d.keys(), key=lambda x: d[x])
        return list(d.values()).count(d[j])
