class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        for num in nums:
            # 각 숫자에 대해 [num-k, num+k] 구간을 추가
            events.append((num - k, 1))  # 시작점에 1 추가
            events.append((num + k + 1, -1))  # 끝점 바로 다음에 -1 추가
        
        # 이벤트를 정렬
        events.sort()
        
        # 스위핑을 통해 겹치는 구간의 최대값 계산
        current = 0
        max_beauty = 0
        for _, change in events:
            current += change
            max_beauty = max(max_beauty, current)
        
        return max_beauty
