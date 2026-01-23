class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        def func(arr):
            n = len(arr)
            index, value = 0, float("inf")
            count = 0

            for i in range(n - 1):
                a, b = nums[i], nums[i + 1]
                if a > b:
                    count += 1
                if value > a + b:
                    index = i
                    value = a + b

            if count > 0:
                arr[index] = arr[index] + arr[index + 1]
                del arr[index + 1]
                return arr

            return None

        count = -1
        while nums:
            count += 1
            nums = func(nums)
            # print(nums)

        return count
