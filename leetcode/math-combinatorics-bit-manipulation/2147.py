class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # 1. 모든 좌석(S)의 인덱스를 저장합니다.
        seats = [i for i, char in enumerate(corridor) if char == "S"]

        # 2. 예외 처리: 좌석이 없거나 홀수 개인 경우
        if len(seats) == 0 or len(seats) % 2 != 0:
            return 0

        res = 1
        MOD = 10**9 + 7

        # 3. 두 번째 쌍부터 시작하여, 이전 쌍과의 거리를 계산합니다.
        # 인덱스 배열 예시: [s0, s1, s2, s3, s4, s5]
        # 우리가 필요한 거리: (s2 - s1), (s4 - s3) ...
        # 즉, (짝수 번째 인덱스 - 바로 앞의 홀수 번째 인덱스)
        for i in range(2, len(seats), 2):
            length = seats[i] - seats[i - 1]
            res = (res * length) % MOD

        return res
