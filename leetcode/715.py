import bisect


class RangeModule:

    def __init__(self):
        # 구간을 일렬로 저장할 리스트 (항상 정렬 상태 유지)
        # 예: [10, 20, 30, 40] -> [10, 20) 구간과 [30, 40) 구간이 존재함
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        # 1. 삽입할 위치 찾기
        i = bisect.bisect_left(self.track, left)
        j = bisect.bisect_right(self.track, right)

        # 2. 새로운 구간 병합을 위한 임시 리스트
        subtrack = []

        # left가 구간 외부에 있다면(짝수 인덱스), left를 시작점으로 추가
        if i % 2 == 0:
            subtrack.append(left)
        # (만약 i가 홀수라면, left는 기존 구간 내부에 있으므로 기존 시작점을 유지 -> 추가 안 함)

        # right가 구간 외부에 있다면(짝수 인덱스), right를 끝점으로 추가
        if j % 2 == 0:
            subtrack.append(right)
        # (만약 j가 홀수라면, right는 기존 구간 내부에 있으므로 기존 끝점을 유지 -> 추가 안 함)

        # 3. 기존의 겹치는 부분들을 모두 제거하고 새 범위로 대체
        self.track[i:j] = subtrack

    def removeRange(self, left: int, right: int) -> None:
        # 1. 제거할 범위 위치 찾기
        i = bisect.bisect_left(self.track, left)
        j = bisect.bisect_right(self.track, right)

        subtrack = []

        # left가 구간 내부에 있다면(홀수 인덱스),
        # 기존 구간이 left에서 잘리므로 left가 앞 구간의 새로운 끝점이 됨
        if i % 2 == 1:
            subtrack.append(left)

        # right가 구간 내부에 있다면(홀수 인덱스),
        # 기존 구간이 right에서 다시 시작하므로 right가 뒷 구간의 새로운 시작점이 됨
        if j % 2 == 1:
            subtrack.append(right)

        # 3. 해당 범위를 대체 (구간 삭제 혹은 분할 효과)
        self.track[i:j] = subtrack

    def queryRange(self, left: int, right: int) -> bool:
        # 1. left와 right의 위치 확인
        i = bisect.bisect_right(self.track, left)
        j = bisect.bisect_left(self.track, right)

        # 조건 1: i == j (left와 right가 같은 구간 덩어리 안에 있어야 함)
        # 조건 2: i % 2 == 1 (그 덩어리가 '시작~끝' 사이의 구간이어야 함. 즉, 구간 내부)
        return i == j and i % 2 == 1
