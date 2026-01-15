import math


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            while stack:
                top = stack[-1]
                g = math.gcd(top, num)

                # 서로소가 아니라면 (GCD > 1)
                if g > 1:
                    stack.pop()  # 기존 top 제거
                    # LCM 계산: (A * B) // GCD
                    num = (top * num) // g
                    # 여기서 멈추지 않고, 합쳐진 num이
                    # 스택의 그 다음 요소와 또 합쳐질 수 있는지 계속 while 루프를 돕니다.
                else:
                    # 서로소라면 병합을 멈춤
                    break

            # 병합이 끝난(혹은 병합할 게 없는) 최종 num을 스택에 추가
            stack.append(num)

        return stack
