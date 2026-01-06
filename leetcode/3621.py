import math


class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        # k가 0인 경우: depth가 0인 수는 1 하나뿐입니다.
        if k == 0:
            return 1

        # 1. 작은 숫자들에 대해 depth 미리 계산
        # n이 최대 10^18이라도 비트 수는 60을 넘지 않으므로 64까지만 계산하면 충분합니다.
        # dp[i] = 숫자 i의 depth
        dp = {1: 0}

        # 타겟 비트 수(c) 후보군: depth가 k-1인 c를 찾기 위함
        target_bit_counts = []

        # 2부터 64까지 depth 계산 (비트 수가 64를 넘을 일은 거의 없음)
        # 실제로는 n의 비트 길이만큼만 필요합니다.
        max_bits = n.bit_length()

        for i in range(2, max_bits + 1):
            c = bin(i).count("1")
            dp[i] = dp[c] + 1
            if dp[i] == k - 1:
                target_bit_counts.append(i)

        # 예외: 만약 k=1이라면, 위 루프에서 dp[1]=0 == k-1 조건을 검사하지 못했으므로 추가
        # dp[1]은 0이므로, k-1 == 0 (즉 k=1)일 때 타겟 비트 수에 1이 포함되어야 함
        if k == 1:
            target_bit_counts.append(1)

        # 2. 조합론을 이용해 1~n 사이에서 비트 개수가 c인 숫자의 개수 구하기
        # nCr 함수
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return math.comb(n, r)

        def count_numbers_with_c_bits(limit_n, c):
            # limit_n까지 숫자 중 비트가 c개인 수의 개수 반환
            s = bin(limit_n)[2:]  # 2진수 문자열
            length = len(s)
            count = 0
            set_bits_so_far = 0

            for i, bit in enumerate(s):
                if bit == "1":
                    # 현재 자리에 0을 넣는 경우:
                    # 남은 자리(length - 1 - i) 중 필요한 비트 수(c - set_bits_so_far)를 뽑는 경우의 수
                    remaining_pos = length - 1 - i
                    needed = c - set_bits_so_far
                    count += nCr(remaining_pos, needed)

                    # 현재 자리에 1을 넣는 경우(계속 진행):
                    set_bits_so_far += 1

                # 가지치기: 이미 필요한 비트 수를 초과했거나, 남은 자리에 다 채워도 부족한 경우
                if set_bits_so_far > c:
                    break

            # 마지막으로 n 자기 자신이 c개의 비트를 가졌는지 확인
            if set_bits_so_far == c:
                count += 1

            return count

        ans = 0
        for c in target_bit_counts:
            if c > max_bits:
                continue
            ans += count_numbers_with_c_bits(n, c)

        # 3. 예외 처리 보정 (x=1)
        # 위 로직은 x=1도 "비트 개수가 1개"이므로 세는 경우가 있음.
        # 하지만 1의 depth는 0임.
        # 만약 k=1이라면, 로직은 c=1인 수(1, 2, 4...)를 셈. 여기엔 1이 포함됨.
        # 1은 실제 depth가 0이므로 k=1의 결과에서 제외해야 함.
        # 반대로 k=0이라면 정답은 1이어야 함 (맨 위에서 처리함).

        # 즉, target_bit_counts에 1이 포함되어 있다면(k=1인 경우),
        # count_numbers_with_c_bits(n, 1)에는 숫자 1이 포함되어 계산됨.
        # 하지만 숫자 1의 실제 depth는 0이므로 k=1의 해답이 아님. -> -1 해줌.
        if 1 in target_bit_counts:
            ans -= 1

        return ans
