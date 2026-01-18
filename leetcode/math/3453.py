from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 1. 전체 넓이의 절반 계산
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2

        # 2. 이벤트 생성 (y좌표, 가로 폭 변화량)
        # 사각형의 x좌표는 넓이 계산에 영향이 없으므로 무시합니다.
        # (y, l) -> y 지점에서 폭이 l 만큼 늘어남
        # (y+l, -l) -> y+l 지점에서 폭이 l 만큼 줄어듦
        events = []
        for _, y, l in squares:
            events.append((y, l))
            events.append((y + l, -l))

        # 3. y좌표 기준으로 정렬
        events.sort(key=lambda x: x[0])

        current_width = 0  # 현재 y 위치에서의 유효한 가로 폭의 합
        accumulated_area = 0  # 지금까지 누적된 넓이
        prev_y = events[0][0]  # 이전 y 좌표

        # 4. 이벤트 순회 (스위핑)
        for y, diff in events:
            # y 좌표가 이동했다면, 그 사이 구간의 넓이를 누적
            height = y - prev_y
            if height > 0:
                # 현재 구간의 넓이
                segment_area = current_width * height

                # 목표 넓이에 도달했는지 확인
                if accumulated_area + segment_area >= target:
                    # 정확한 y 위치 계산 (선형 보간)
                    # 남은 넓이 = target - accumulated_area
                    # 필요한 높이 = 남은 넓이 / current_width
                    return prev_y + (target - accumulated_area) / current_width

                accumulated_area += segment_area

            # 상태 업데이트
            current_width += diff
            prev_y = y

        return float(prev_y)
