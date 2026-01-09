class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ans = 0
        cur_idx = 0
        n = len(nums)

        # 배열을 한 번만 순회 (O(N))
        for i in range(1, n):
            # 현재 값보다 더 큰 값을 만나면 바로 점프 (가중치 교체)
            if nums[i] > nums[cur_idx]:
                ans += (i - cur_idx) * nums[cur_idx]
                cur_idx = i

        # 순회가 끝난 후, 아직 마지막 인덱스에 도달하지 않았다면
        # 현재 위치에서 마지막 인덱스까지 한 번에 점프
        ans += (n - 1 - cur_idx) * nums[cur_idx]

        return ans
