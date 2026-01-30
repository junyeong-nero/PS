class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # positive +3 / negative -1

        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

        def get_score(s):
            score = 0
            for word in s.split():
                if word in positive_feedback:
                    score += 3
                if word in negative_feedback:
                    score -= 1
            
            return score

        q = []
        n = len(student_id)
        for i in range(n):
            score = get_score(report[i])
            heappush(q, (-score, student_id[i]))
        
        res = []
        for _ in range(k):
            neg_score, _id = heappop(q)
            res.append(_id)

        return res
