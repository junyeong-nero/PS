from collections import Counter
from functools import cache
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        target_cnt = Counter(target)

        # 1. 전처리: target에 없는 문자를 가진 스티커 내용은 제거하여 최적화
        # 스티커를 Counter 객체 리스트로 변환
        sticker_counts = []
        for s in stickers:
            # target에 있는 문자만 남김
            c = Counter(s) & target_cnt
            if c:
                # (중요) A 스티커가 B 스티커에 완전히 포함(dominated)된다면 A는 필요 없음
                # 하지만 구현 복잡도를 위해 일단 단순 필터링만 수행해도 충분히 빠름
                sticker_counts.append(c)

        # 2. 메모이제이션을 위한 DFS 함수 (비트마스크 사용)
        # mask: 현재 채워야 할 target의 인덱스들을 비트로 표현 (1이면 아직 필요함, 0이면 채워짐)
        @cache
        def dfs(mask):
            # 모든 비트가 0이면(모든 문자를 채움) 0 반환
            if mask == 0:
                return 0

            res = float("inf")

            # 3. 가지치기 (핵심 최적화):
            # 현재 마스크에서 가장 먼저 등장하는 '아직 필요한 문자'의 인덱스를 찾음
            # 이 문자를 포함하지 않는 스티커는 굳이 시도해볼 필요가 없음 (탐색 공간 대폭 축소)
            first_needed_idx = 0
            while not (mask & (1 << first_needed_idx)):
                first_needed_idx += 1

            first_needed_char = target[first_needed_idx]

            # 해당 문자를 가진 스티커만 시도
            for s_count in sticker_counts:
                if first_needed_char not in s_count:
                    continue

                # 스티커 적용 후 새로운 마스크 계산
                new_mask = mask
                s_count_copy = s_count.copy()

                # target의 각 자리를 순회하며 스티커로 지울 수 있는지 확인
                for i in range(n):
                    # 현재 i번째 자리가 아직 필요하고(mask의 i비트가 1), 스티커에 해당 문자가 남아있다면
                    if (mask >> i) & 1 and s_count_copy[target[i]] > 0:
                        s_count_copy[target[i]] -= 1
                        new_mask &= ~(1 << i)  # i번째 비트를 0으로 끔 (채워짐)

                # 다음 상태로 전이
                res = min(res, 1 + dfs(new_mask))

            return res

        # 초기 상태: 모든 비트가 1 (1을 n번 시프트하고 1을 뺌)
        # 예: n=3 -> 1000 - 1 = 0111
        initial_mask = (1 << n) - 1
        ret = dfs(initial_mask)

        return ret if ret != float("inf") else -1
