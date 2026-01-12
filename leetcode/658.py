class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        n = len(arr)
        first_index = bisect_left(arr, x)
        start, end = max(first_index - k, 0), min(first_index + k, n)

        temp = [(abs(arr[i] - x), arr[i]) for i in range(start, end)]
        temp = sorted(temp)
        return sorted([elem[1] for elem in temp[:k]])
