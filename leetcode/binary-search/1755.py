import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def get_subset_sums(arr):
            res = {0}
            for x in arr:
                res |= {s + x for s in res}
            return sorted(list(res))

        n = len(nums)
        left_sums = get_subset_sums(nums[:n//2])
        right_sums = get_subset_sums(nums[n//2:])
        
        ans = float('inf')
        for s in left_sums:
            target = goal - s
            # right_sums에서 target과 가장 가까운 값 찾기
            idx = bisect.bisect_left(right_sums, target)
            
            # 인덱스 위치(idx)와 그 직전 위치(idx-1) 확인
            if idx < len(right_sums):
                ans = min(ans, abs(target - right_sums[idx]))
            if idx > 0:
                ans = min(ans, abs(target - right_sums[idx-1]))
                
        return ans
