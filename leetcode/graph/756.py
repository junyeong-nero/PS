class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict

        # Build dictionary: two chars -> possible upper chars
        d = defaultdict(list)
        for a, b, c in allowed:
            d[a + b].append(c)

        memo = {}  # row 문자열 → 가능한 상위 row 존재 여부 캐싱

        def can_build(row):
            # 만약 row를 이전에 계산했다면 바로 반환
            if row in memo:
                return memo[row]

            if len(row) == 1:
                memo[row] = True
                return True

            # 다음 row를 백트래킹으로 생성
            def dfs(idx, next_row):
                if idx == len(row) - 1:
                    # 생성된 next_row에 대해 계속 위로 올라가기
                    if can_build(next_row):
                        return True
                    return False

                key = row[idx : idx + 2]
                if key not in d:
                    return False

                for c in d[key]:
                    if dfs(idx + 1, next_row + c):
                        return True
                return False

            memo[row] = dfs(0, "")
            return memo[row]

        return can_build(bottom)
