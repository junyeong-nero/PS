from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A)
        m = len(A[0])
        res = 0

        # sorted_rows[i]가 True라면 A[i] < A[i+1]이 이미 확정되었다는 의미입니다.
        sorted_rows = [False] * (n - 1)

        # 각 열(column)을 하나씩 검사합니다.
        for j in range(m):
            should_delete = False

            # 1. 현재 열을 유지했을 때 정렬 순서가 어긋나는지 확인합니다.
            for i in range(n - 1):
                # 이전 열들까지 아직 순서가 확정되지 않았는데(!sorted_rows[i])
                # 현재 열에서 앞 문자열이 뒤보다 크다면 정렬 위반입니다.
                if not sorted_rows[i] and A[i][j] > A[i + 1][j]:
                    should_delete = True
                    break

            # 2. 정렬 위반이라면 해당 열은 삭제하고 결과값을 증가시킵니다.
            if should_delete:
                res += 1
                continue

            # 3. 열을 유지하기로 했다면, 이미 순서가 확정된(A[i] < A[i+1]) 행들을 업데이트합니다.
            for i in range(n - 1):
                if A[i][j] < A[i + 1][j]:
                    sorted_rows[i] = True

        return res
