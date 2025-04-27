class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        s1 = max(str1, str2, key = lambda x: len(x))
        s2 = min(str1, str2, key = lambda x: len(x))

        # check subsequences
        def check(s1, s2):
            n1, n2 = len(s1), len(s2)
            i = j = 0
            while i < n1 and j < n2:
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return s1 + s2[j:]

        n2 = len(s2)
        res = s1 + s2

        for i in range(n2):
            for j in range(n2, i, -1):
                s2_ = s2[i:j]
                temp = s2[:i] + check(s1, s2_) + s2[j:]
                print(s2_, temp)
                if len(temp) < len(res):
                    res = temp

        
        return res
