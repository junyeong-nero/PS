class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = total = 0

        while total < target:
            step += 1
            total += step

        # 결국 step 이 늘어지만, target 을 넘어선 이후로
        # 이전의 steps 중에서 일부를 flipping 하여 해결할 수 있다.
        # 하지만 flipping 하게 되면 원래 수에서 elem * 2 만큼 변화가 일어나기 때문에
        # 차이가 1 인 경우에는 새로운 step을 추가해서 처리해야 한다.

        # 11 = 1 - 2 + 3 + 4 + 5
        # 9  = 1 + 2 + 3 + 4 - 5 + 6

        while (total - target) % 2 != 0:
            step += 1
            total += step

        return step
