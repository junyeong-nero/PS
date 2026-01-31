class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0] * n
        for cur, tar in enumerate(edges):
            score[tar] += cur
        
        # print(score)
        return max(range(n), key=lambda x: score[x])
