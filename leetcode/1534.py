class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        n = len(arr)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x = abs(arr[i] - arr[j])
                    y = abs(arr[j] - arr[k])
                    z = abs(arr[i] - arr[k])
                    if x <= a and y <= b and z <= c:
                        res += 1 

        return res