import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        # 가로(w)는 오름차순, 가로가 같으면 세로(h)는 내림차순 정렬
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # 세로(h) 값들에 대해서만 LIS 구하기
        heights = [envelopes[i][1] for i in range(len(envelopes))]

        # LIS를 위한 tails (이진 탐색 활용)
        tails = []
        for h in heights:
            idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h

        return len(tails)
