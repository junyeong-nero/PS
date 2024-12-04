# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

import functools
from typing import List
from collections import Counter

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:   
        
        m, n = len(str1), len(str2)
        if m < n:
            return False
        
        def dfs(cur, index, jump):
            if jump > m - n:
                return False
            if cur == len(str2):
                return True
            if index >= len(str1):
                return False
            
            char = str1[index]
            new_char = chr(ord(char) + 1) if char != 'z' else 'a'
            
            if char == str2[cur] and dfs(cur + 1, index + 1, jump):
                return True
            elif new_char == str2[cur] and dfs(cur + 1, index + 1, jump):
                return True
            elif dfs(cur, index + 1, jump + 1):
                return True
            
            return False
        
        return dfs(0, 0, 0)
    
        
if __name__ == '__main__':
    # res = Solution().canMakeSubsequence('abc', 'ad')
    # res = Solution().canMakeSubsequence('zc', 'ad')   
    res = Solution().canMakeSubsequence('lssxrgjreysgpgh', 'ltsjssgh')
    print(res)