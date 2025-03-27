class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        m = len(nums)

        left, right = Counter(), Counter(nums)
        left_size, right_size = 0, m
        left_dominant, right_dominant = -1, max(right.keys(), key=lambda x: right[x])
        # print(right_dominant)

        for i in range(m):
            elem = nums[i]
            left[elem] += 1
            left_size += 1
            if left[elem] * 2 > left_size:
                left_dominant = elem
            elif left[left_dominant] <= left_size:
                left_dominant = -1

            right[elem] -= 1
            right_size -= 1
            if right[elem] * 2 > right_size:
                right_dominant = elem
            elif right[right_dominant] <= right_size:
                right_dominant = -1
            
            if left_dominant == right_dominant and left_dominant != -1:
                # print(left, left_dominant)
                # print(right, right_dominant)
                return i
        
        return -1
        
