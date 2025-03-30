class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        n = len(s)
        counter = Counter()
        for i in range(n - 9):
            target = s[i:i + 10]
            counter[target] += 1
        
        return [key for key, value in counter.items() if value >= 2]