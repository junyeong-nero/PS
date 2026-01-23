from math import comb


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        # 1. 정렬: 수의 '순서'가 아닌 '크기'가 중요합니다.
        # 정렬을 해야 인덱스(i)만으로 내 왼쪽에 나보다 작은 수가 몇 개인지,
        # 내 오른쪽에 나보다 큰 수가 몇 개인지 알 수 있습니다.
        nums.sort()

        total_sums = 0
        MOD = 10**9 + 7

        # quantity: 현재 검사하는 숫자(피벗) 외에 '추가로 선택할 수 있는 수'들의 조합의 합입니다.
        # 초기값 1: 나 자신만 선택하는 경우 (nC0 = 1). 즉, 부분 수열의 크기가 1인 경우.
        quantity = 1

        # nums의 길이만큼 반복하지만, 사실상 매 반복마다
        # '앞에서 i번째 숫자'와 '뒤에서 i번째 숫자'를 동시에 처리합니다.
        for i in range(len(nums)):
            # nums[i]: 오름차순의 앞에서 i번째 수 (점점 커짐)
            #   -> 이 수는 자신의 왼쪽에 있는 i개의 작은 수들과 조합되어 '최대값'으로 쓰입니다.

            # nums[-i-1]: 오름차순의 뒤에서 i번째 수 (점점 작아짐, 즉 큰 수들)
            #   -> 이 수는 자신의 오른쪽에 있는 i개의 큰 수들과 조합되어 '최소값'으로 쓰입니다.

            # [핵심]
            # nums[i]가 '최대값'이 되기 위해 선택할 수 있는 후보의 개수(왼쪽 i개)와
            # nums[-i-1]가 '최소값'이 되기 위해 선택할 수 있는 후보의 개수(오른쪽 i개)는
            # 동일하게 'i개'입니다. 따라서 가능한 부분 수열의 경우의 수(quantity)도 같습니다.

            contribution = quantity * (nums[i] + nums[-i - 1])
            total_sums = (total_sums + contribution) % MOD

            # [다음 라운드 준비: quantity 업데이트]
            # 현재 quantity는 i개의 후보 중 0~(k-1)개를 뽑는 경우의 수의 합입니다.
            # 다음 루프(i+1)에서는 후보가 하나 늘어나므로, 경우의 수를 갱신해야 합니다.
            # 공식: S(i+1) = 2 * S(i) - comb(i, k-1)
            # 이유: 원소가 하나 추가되면 기본적으로 경우의 수는 2배(포함/미포함)가 되지만,
            #       '최대 크기 k' 제한 때문에 (k-1)개를 이미 뽑은 상태에서 새 원소를
            #       추가하여 크기가 k+1이 되는 경우는 제외해야 합니다.
            if i < len(nums) - 1:  # 마지막 루프가 아닐 때만 계산 (시간 절약)
                quantity = (2 * quantity - comb(i, k - 1)) % MOD

        return total_sums
