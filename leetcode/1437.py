class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        arr = []
        n = len(nums)
        for index, value in enumerate(nums):
            if value == 1:
                arr.append(index)

        arr = [arr[i + 1] - arr[i] - 1 for i in range(len(arr) - 1)]
        # print(arr)
        return all([elem >= k for elem in arr])
