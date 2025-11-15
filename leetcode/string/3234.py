import math


class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        """
        주어진 이진 문자열에서 '지배적인' 부분 문자열의 개수를 계산합니다.
        '지배적인' 부분 문자열은 '0'의 개수를 Z라고 할 때, '1'의 개수가 Z*Z 이상인 경우를 말합니다.
        """
        n = len(s)

        # Zmax는 부분 문자열에 포함될 수 있는 '0'의 최대 개수입니다.
        # '0'의 개수가 cnt0일 때, '1'의 개수는 최소 cnt0*cnt0이어야 합니다.
        # 따라서 부분 문자열의 최소 길이는 cnt0*cnt0 + cnt0 = cnt0*(cnt0+1)입니다.
        # n >= cnt0*(cnt0+1) 이어야 하므로, 이 부등식을 풀면 Zmax를 구할 수 있습니다.
        Zmax = int((math.sqrt(1.0 + 4 * n) - 1) / 2)

        # 문자열 s에서 '0'의 인덱스를 p0 리스트에 저장합니다.
        p0 = [i for i, char in enumerate(s) if char == "0"]
        p0.append(n)  # 계산 편의를 위해 문자열 길이 n을 sentinel 값으로 추가합니다.

        ans = 0
        front = 0  # p0 리스트에서 현재 부분 문자열의 시작점 바로 다음에 오는 '0'의 인덱스를 가리킵니다.

        # 모든 가능한 시작점 l에 대해 반복합니다.
        for l in range(n):
            # 현재 시작점 l이 p0[front]를 지났다면 front를 이동시킵니다.
            # 즉, l보다 작은 인덱스의 '0'들은 더 이상 고려하지 않습니다.
            while front < len(p0) and p0[front] < l:
                front += 1

            prev = l  # 이전 '0'의 위치를 추적하기 위한 변수, 초기값은 시작점 l

            # 현재 시작점 l 이후의 '0'들을 순회합니다.
            for p in range(front, len(p0)):
                # 이 세그먼트 [l, r)는 cnt0개의 '0'을 가집니다.
                cnt0 = p - front
                r = p0[p]  # 현재 '0'의 위치 (부분 문자열의 끝 경계 역할)

                if cnt0 > Zmax:
                    break

                # 지배적인 부분 문자열의 최소 길이는 cnt0 * (cnt0 + 1)입니다.
                # 또한, 이전 '0'의 위치(prev)를 포함해야 하므로 길이는 prev - l + 1 이상이어야 합니다.
                minLen = max(prev - l + 1, cnt0 * (cnt0 + 1))

                # s[l..t] 형태의 지배적인 부분 배열을 고려합니다.
                # 여기서 cnt0개의 '0'을 포함하고 t < r 입니다.
                # 가능한 끝점의 개수를 계산하여 ans에 더합니다.
                # (r - l)은 현재 [l, r) 구간의 길이입니다.
                # minLen은 이 구간에서 유효한 부분 문자열이 되기 위한 최소 길이입니다.
                # 따라서 (r - l) - minLen + 1은 가능한 유효한 끝점의 개수가 됩니다.
                ans += max(0, (r - l) - minLen + 1)
                prev = r  # prev를 현재 '0'의 위치로 업데이트합니다.

        return ans
