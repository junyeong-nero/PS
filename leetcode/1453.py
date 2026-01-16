import math


class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        # 점이 1개 이하면 바로 리턴
        if n == 1:
            return 1

        res = 1

        # 두 점 사이의 거리를 구하는 함수
        def get_dist_sq(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        # 모든 점의 쌍(i, j)을 확인
        for i in range(n):
            for j in range(i + 1, n):
                p1 = darts[i]
                p2 = darts[j]
                d2 = get_dist_sq(p1, p2)

                # 두 점 사이 거리가 지름(2r)보다 크면 두 점을 동시에 포함할 수 없음
                if d2 > (2 * r) ** 2:
                    continue

                # 기하학 공식으로 두 원의 교점(가능한 중심 후보) 구하기
                # 중점 좌표
                mid_x = (p1[0] + p2[0]) / 2
                mid_y = (p1[1] + p2[1]) / 2

                # 피타고라스 정리로 중점에서 원의 중심까지의 거리(h) 구하기
                # h^2 = r^2 - (d/2)^2
                d = math.sqrt(d2)
                h = math.sqrt(r**2 - (d / 2) ** 2)

                # 각도 계산을 이용한 오프셋 (x, y 변화량)
                x_offset = h * (p1[1] - p2[1]) / d
                y_offset = h * (p2[0] - p1[0]) / d

                # 가능한 두 개의 중심 좌표 (c1, c2)
                centers = [
                    (mid_x + x_offset, mid_y + y_offset),
                    (mid_x - x_offset, mid_y - y_offset),
                ]

                # 각 중심에 대해 몇 개의 다트가 포함되는지 카운트
                for center in centers:
                    cnt = 0
                    for k in range(n):
                        # 부동소수점 오차를 고려해 약간의 여유(epsilon)를 주거나
                        # r^2과의 비교를 통해 포함 여부 확인
                        if get_dist_sq(center, darts[k]) <= r**2 + 1e-7:
                            cnt += 1
                    res = max(res, cnt)

        return res
