class Solution:
    def countCollisions(self, directions: str) -> int:
        # 1. 왼쪽 끝의 L들을 잘라내고, 오른쪽 끝의 R들을 잘라냅니다.
        # 이들은 도로 밖으로 나가버리는 차들입니다.
        remaining = directions.lstrip("L").rstrip("R")

        # 2. 남은 구간(remaining)에 있는 차들 중
        # 멈춰있는 차('S')를 제외한 모든 차는 어딘가에 충돌하게 됩니다.
        # 따라서 전체 길이에서 S의 개수를 뺍니다.
        return len(remaining) - remaining.count("S")
