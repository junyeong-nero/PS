class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        ma = max(A)
        res = cur = i = 0
        for j in range(len(A)):
            cur += A[j] == ma
            while cur >= k:
                cur -= A[i] == ma
                i += 1
            res += i
        return res