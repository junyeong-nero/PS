class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:

        # bitwise AND => A & B <= A or B
        # set MSB as same is critique within m elements
        # no O(N^2)

        # choose any m indices, max bitwise AND value =>
        # value * m - sum(value of m indices) <= k
        # vlaue * m <= k + sum(value of m indices)
        # value <= (k + sum(value of m indices)) / m

        # choice any m indices in nums
        # too big...................... O(N^M)?
        # => sorting!, subarray does not matter ordering
        # sliding window with size = m

        if m == 1:
            return max(nums) + k

        nums = sorted(nums)
        n = len(nums)

        window = deque(nums[:m])
        res = max()

        for i in range(n - m):

            temp = (k + sum(window)) // m
            if window[-1] <= k:
                res = max(res, temp)
                print(window, temp)
            else:
                pass

            window.popleft()
            window.append(nums[i + m])

        if window[-1] <= k:
            res = max(res, (k + sum(window)) // m)
        return res


from typing import List


class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:

        # 특정 숫자 x를 mask 패턴을 포함하도록 만들 때 드는 비용 계산
        def get_cost(x, mask):
            cost = 0
            # 상위 비트부터 처리하면서 변경이 일어났는지 체크
            changed = False

            for i in range(32, -1, -1):
                # mask에서 i번째 비트가 켜져 있어야 하는데
                if (mask >> i) & 1:
                    # 1. 이전에 상위 비트를 맞추느라 숫자가 변경된 경우 (하위 비트는 다 0이 됨)
                    if changed:
                        cost += 1 << i
                    # 2. 변경된 적 없지만, 현재 x의 i번째 비트가 0인 경우
                    elif not ((x >> i) & 1):
                        # 해당 비트를 1로 만들고 하위 비트를 0으로 만드는 최소 비용
                        diff = (1 << i) - (x % (1 << i))
                        cost += diff
                        changed = True
            return cost

        ans = 0

        # 30번째 비트부터 0번째 비트까지 내림차순 탐색
        for i in range(32, -1, -1):
            # 현재까지 확정된 답(ans)에 이번 비트(1<<i)를 추가해봄
            target = ans | (1 << i)

            # 모든 숫자에 대해 target을 만들기 위한 비용 계산
            costs = []
            for x in nums:
                costs.append(get_cost(x, target))

            # 비용이 적게 드는 순서대로 m개 선택
            # (전체 정렬 대신 nsmallest를 쓰면 더 빠를 수 있음 O(N))
            costs.sort()

            # 상위 m개의 비용 합이 k 이하라면, 이 비트는 챙길 수 있음
            if sum(costs[:m]) <= k:
                ans = target

        return ans
