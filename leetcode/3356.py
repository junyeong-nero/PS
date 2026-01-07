class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        n = len(nums)

        def can_transform(k):
            # 차분 배열 초기화
            diff = [0] * (n + 1)
            # k개의 쿼리 적용
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            # 누적합을 계산하며 nums[i]와 비교
            current_reduction = 0
            for i in range(n):
                current_reduction += diff[i]
                if current_reduction < nums[i]:
                    return False
            return True

        # 이진 탐색 시작
        left, right = 0, len(queries)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can_transform(mid):
                ans = mid
                right = mid - 1  # 더 작은 k가 있는지 확인
            else:
                left = mid + 1

        return ans
