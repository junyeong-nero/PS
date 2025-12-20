class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        count = 0
        for i in range(m):
            for j in range(n - 1):
                a, b = ord(strs[j][i]), ord(strs[j + 1][i])
                if a > b:
                    count += 1
                    break
        return count
