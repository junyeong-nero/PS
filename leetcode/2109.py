# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        temp = ''
        j = 0
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                j += 1
                temp += ' '
            temp += s[i]
        
        return temp