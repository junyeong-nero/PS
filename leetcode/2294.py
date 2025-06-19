class Solution:
    def partitionArray(self, A, k):
        A.sort()
        res = 1
        mn = mx = A[0]
        for a in A:
            mn = min(mn, a)
            mx = max(mx, a)
            if mx - mn > k:
                res += 1
                mn = mx = a
        return res