class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left, right = [0, 0], [nums.count(0), nums.count(1)]
        scores = [left[0] + right[1]]
        n = len(nums)

        for i in range(n):
            cur = nums[i]
            left[cur] += 1
            right[cur] -= 1
            scores.append(left[0] + right[1])

        value = max(scores)
        res = [i for i in range(len(scores)) if scores[i] == value]
        return res
