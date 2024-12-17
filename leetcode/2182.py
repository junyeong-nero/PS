from itertools import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        s = Counter(s)
        keys = sorted(s.keys(), reverse=True)
        n = len(keys)
        temp = ''
        for i in range(n - 1):
            check = True
            key = keys[i]
            while s[key] > repeatLimit:
                new_key = ''
                for j in range(i + 1, n):
                    if s[keys[j]] > 0:
                        new_key = keys[j]
                        break

                if new_key == '':
                    check = False
                    break
                
                s[key] -= repeatLimit
                temp += key * repeatLimit   
                s[new_key] -= 1
                temp += new_key
            
            if check:
                temp += key * s[key]
                s[key] = 0
                

        for i in range(n):
            temp += keys[i] * min(s[keys[i]], repeatLimit)
        return temp
        