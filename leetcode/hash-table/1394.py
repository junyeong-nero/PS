class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        res = -1
        for key, value in counter.items():
            if key == value:
                res = max(res, key)

        return res
