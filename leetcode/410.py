class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 1. 누적 합 배열 (Prefix Sum) 계산
        # prefix[i]는 nums[0]부터 nums[i-1]까지의 합
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # 부분 배열 합을 O(1)에 계산하는 함수
        def get_sum(i, j):
            # nums[i] 부터 nums[j-1] 까지의 합 (j > i)
            return prefix[j] - prefix[i]

        # 2. DP 테이블 초기화
        # dp[i][j]: nums의 첫 i개 원소를 j개의 부분 배열로 분할했을 때,
        # 최대 부분 배열 합의 최솟값.
        # 크기: (n + 1) x (k + 1)
        # float('inf')로 초기화
        dp = [[float("inf")] * (k + 1) for _ in range(n + 1)]

        # 3. 초기 조건 (Base Case)
        # 첫 i개 원소를 1개 부분 배열로 분할하는 경우
        for i in range(1, n + 1):
            dp[i][1] = get_sum(0, i)

        # 4. DP 테이블 채우기
        for j in range(2, k + 1):  # 부분 배열 개수 (2개부터 k개까지)
            for i in range(1, n + 1):  # 고려하는 원소 개수 (1개부터 n개까지)
                # i개 원소를 j개로 분할하려면 최소 j개 원소가 있어야 함
                if i < j:
                    continue

                # p는 j번째(마지막) 부분 배열의 시작 인덱스 (0-based)
                # p는 최소 j-1이어야 함 (첫 p개 원소 dp[p][j-1]을 위해)
                # p는 최대 i-1이어야 함 (마지막 원소 nums[i-1]을 포함하기 위해)
                for p in range(j - 1, i):
                    # j번째 부분 배열의 합: nums[p] ~ nums[i-1]
                    current_subarray_sum = get_sum(p, i)

                    # 점화식: max(이전 최적 값, 현재 부분 배열 합)
                    # 이를 최소화 (min) 하는 p를 찾음
                    candidate = max(dp[p][j - 1], current_subarray_sum)
                    dp[i][j] = min(dp[i][j], candidate)

        # 5. 결과 반환: nums 전체 (n개)를 k개로 분할한 최솟값
        return dp[n][k]
