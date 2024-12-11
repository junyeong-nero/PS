from typing import List

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

    # sorting 
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        max_beauty = 0

        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # Move the left pointer to maintain the valid range
            while nums[right] - nums[left] > 2 * k:
                left += 1
            # Update the maximum beauty based on the current range
            # We do not add 1 here as right is already pointing to one position beyond the valid range.
            max_beauty = max(max_beauty, right - left + 1)

        return max_beauty