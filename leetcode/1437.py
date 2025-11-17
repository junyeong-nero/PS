class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = None
        n = len(nums)
        for index, value in enumerate(nums):
            if value == 0:
                continue
            if prev:
                cur = index - prev - 1
                print(cur)
                if cur < k:
                    return False

            prev = index

        return True
