class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        # 1. 전체 배열의 Bitwise AND 계산
        total_and = -1  # 모든 비트가 1인 상태 (Python에서는 -1이 무한한 1 비트를 가짐)
        for num in nums:
            total_and &= num

        # 2. 전체 AND가 0이 아니라면, 쪼개서 이득을 볼 수 없으므로 1 리턴
        # (쪼개면 Sum of ANDs가 오히려 증가하거나 같음)
        if total_and != 0:
            return 1

        # 3. 전체 AND가 0이라면, AND가 0이 되는 구간을 최대한 많이 만듦 (Greedy)
        count = 0
        current_and = -1

        for num in nums:
            current_and &= num
            # 현재까지의 누적 AND가 0이 되면 하나의 부분 배열 완성
            if current_and == 0:
                count += 1
                current_and = -1  # 다음 부분 배열을 위해 초기화

        return count


# class Solution:
#     def maxSubarrays(self, nums: List[int]) -> int:

#         n = len(nums)
#         min_score = float("inf")
#         min_count = 0

#         @cache
#         def dfs(cur, value, score=0, count=0):
#             nonlocal min_score, min_count

#             if cur == n:
#                 score += value
#                 count += 1
#                 if score < min_score:
#                     min_score = score
#                     min_count = 0
#                 if score == min_score:
#                     min_count += 1
#                 return

#             if score > min_score:
#                 return

#             dfs(cur + 1, value & nums[cur], score, count)
#             dfs(cur + 1, nums[cur], score + value, count + 1)

#         dfs(0, (1 << 20) - 1)
#         print(min_score, min_count)
#         return min_count
