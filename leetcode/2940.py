from collections import deque
from bisect import bisect_right
from operator import itemgetter
from typing import List

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # 결과 리스트 초기화 (queries 크기와 동일, 초기값은 0)
        res = [0] * len(queries)
        # 특정 조건을 만족하는 쿼리의 인덱스를 저장할 리스트
        idx = []

        # 각 쿼리에 대해 처리
        for i, q in enumerate(queries):
            # 쿼리를 정렬하여 작은 값을 a, 큰 값을 b로 설정
            a, b = sorted(q)
            
            # a와 b가 같거나 a의 높이가 b의 높이보다 작으면 b를 결과로 저장
            if a == b or heights[a] < heights[b]:
                res[i] = b
            else:
                # 그렇지 않으면 해당 쿼리의 정보를 idx에 저장
                idx.append((a, b, i))

        # heights 리스트를 뒤에서부터 처리하기 위한 변수와 deque 초기화
        j = len(heights) - 1
        mono = deque()

        # idx 리스트를 b값을 기준으로 내림차순 정렬하여 처리
        for a, b, i in sorted(idx, key=itemgetter(1), reverse=True):
            # j가 b보다 큰 동안 높이를 처리
            while j > b:
                # 현재 높이보다 작은 높이를 가진 인덱스를 제거 (단조 감소 유지)
                while mono and heights[mono[0]] < heights[j]:
                    mono.popleft()
                # 현재 인덱스를 mono의 맨 앞에 추가
                mono.appendleft(j)
                j -= 1

            # heights[a]보다 크거나 같은 첫 번째 인덱스를 찾음
            k = bisect_right(mono, heights[a], key=lambda x: heights[x])
            # 해당 인덱스가 없으면 -1, 있으면 해당 값을 결과에 저장
            res[i] = -1 if k == len(mono) else mono[k]

        return res
