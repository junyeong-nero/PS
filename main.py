from typing import List

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

if __name__ == '__main__':
    res = Solution().addSpaces('helloworld', [5])
    print(res)