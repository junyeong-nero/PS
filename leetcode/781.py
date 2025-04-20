class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        res = 0
        for key, value in counter.items():
            res += math.ceil(value / (key + 1)) * (key + 1)

        return res