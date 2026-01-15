from functools import cache
from typing import List


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)

        # [최적화 1] 곱(Product)과 상관없이, 남은 숫자들로 목표 합 k를 만들 수 있는지 확인하는 함수
        # 상태 공간이 (index, current_sum, turn)으로 훨씬 작음
        @cache
        def can_make_sum(idx, current_sum, turn):
            if idx == n:
                return current_sum == k

            # 1. Skip current
            if can_make_sum(idx + 1, current_sum, turn):
                return True

            # 2. Pick current (Product 계산 안 함)
            if can_make_sum(idx + 1, current_sum + turn * nums[idx], -turn):
                return True

            return False

        @cache
        def dfs(cur, total=0, prod=float("-inf"), turn=1):
            if cur >= n:
                if total == k and prod <= limit:
                    return prod
                return float("-inf")

            res = float("-inf")

            # 현재 상태가 조건 만족 시 결과 갱신
            if total == k and prod <= limit:
                res = prod

            # 1. Skip current number
            res = max(res, dfs(cur + 1, total, prod, turn))

            # 2. Pick current number
            num = nums[cur]

            if num == 0:
                # [핵심 수정] 0을 선택하는 경우 -> 곱은 무조건 0이 됨
                # 0이 limit 범위 내라면, 더 이상 곱셈 탐색을 하지 않고 '합'만 맞는지 확인
                if 0 <= limit:
                    # 0을 선택했으므로 total은 그대로, turn은 반전됨
                    if can_make_sum(cur + 1, total, -turn):
                        res = max(res, 0)
                # 0을 선택한 경로는 여기서 끝냄 (더 깊이 들어가지 않음)
            else:
                # 0이 아닌 경우 -> 일반적인 탐색
                new_prod = num if prod == float("-inf") else prod * num
                res = max(res, dfs(cur + 1, total + turn * num, new_prod, -turn))

            return res

        res = dfs(0)
        return -1 if res == float("-inf") else res


from collections import defaultdict
from typing import List


class Solution:
    def maxProduct(self, A: List[int], k: int, limit: int) -> int:
        # pos: 마지막 연산이 '뺄셈(-)'으로 끝난 상태들 (sum -> set of products)
        #      즉, 다음에는 '덧셈(+)'을 할 차례인 상태들의 모음
        # neg: 마지막 연산이 '덧셈(+)'으로 끝난 상태들 (sum -> set of products)
        #      즉, 다음에는 '뺄셈(-)'을 할 차례인 상태들의 모음
        pos, neg = defaultdict(set), defaultdict(set)

        # 배열의 모든 숫자를 순회 (현재 숫자: a)
        for a in A:
            # 1. '뺄셈'을 수행할 차례 (neg -> pos2)
            # 이전에 덧셈으로 끝난 상태(neg)에서 현재 값 a를 뺍니다.
            # 결과적으로 마지막이 뺄셈인 상태(pos2)가 만들어집니다.
            pos2 = {s - a: {p * a for p in neg[s] if p * a <= limit} for s in neg}

            # 2. '덧셈'을 수행할 차례 (pos -> neg2)
            # 이전에 뺄셈으로 끝난 상태(pos)에서 현재 값 a를 더합니다.
            # 결과적으로 마지막이 덧셈인 상태(neg2)가 만들어집니다.
            neg2 = {s + a: {p * a for p in pos[s] if p * a <= limit} for s in pos}

            # 3. 기존 상태 업데이트 (Merge)
            # 새로 계산된 pos2 상태들을 기존 pos에 합칩니다.
            for s in pos2:
                # a가 0이면 곱은 무조건 0이 됩니다. (a가 0일 때의 예외 처리)
                # a가 0이 아니면 계산된 곱들의 집합(pos2[s])을 그대로 가져옵니다.
                pos[s] |= pos2[s] if a else {0}

            # 새로 계산된 neg2 상태들을 기존 neg에 합칩니다.
            for s in neg2:
                neg[s] |= neg2[s] if a else {0}

            # 4. 새로운 수열의 시작 (Initialization)
            # 이 숫자(a)부터 새로운 부분 수열을 시작하는 경우입니다.
            # 수열의 시작은 항상 양수(+)이므로, neg 딕셔너리에 추가합니다.
            # (즉, +a로 시작했으므로 다음은 뺄셈 차례 -> neg에 저장)
            if a <= limit:
                neg[a].add(a)

        # 5. 결과 도출
        # 합이 k인 모든 경우(pos[k]와 neg[k])를 합칩니다.
        # 합집합이 비어있지 않다면 그 중 최댓값을, 비어있다면 -1을 반환합니다.
        res = pos[k] | neg[k]
        return max(res) if res else -1
