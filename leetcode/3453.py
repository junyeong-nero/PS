from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 전체 넓이 계산
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2

        # 이분 탐색 범위 설정
        min_y = min(y for _, y, _ in squares)
        max_y = max(y + l for _, y, l in squares)

        left, right = min_y, max_y

        # y선 아래의 넓이를 구하는 함수 (단순 반복)
        def get_area_below(y):
            area = 0
            for _, sy, l in squares:
                top = sy + l
                # 1. 사각형이 완전히 y 아래에 있는 경우
                if top <= y:
                    area += l * l
                # 2. 사각형이 y 선에 걸쳐 있는 경우
                elif sy < y < top:
                    area += (y - sy) * l
                # 3. 사각형이 완전히 y 위에 있는 경우 -> area += 0
            return area

        # 이분 탐색 (Binary Search)
        # 반복 횟수로 제어하면 무한 루프 방지 및 정밀도 확보에 유리합니다 (보통 100회면 충분)
        for _ in range(100):
            mid = (left + right) / 2
            current_area = get_area_below(mid)

            if current_area < target:
                left = mid  # 넓이가 부족하므로 선을 더 위로
            else:
                right = mid  # 넓이가 넘치므로 선을 더 아래로

        return left
