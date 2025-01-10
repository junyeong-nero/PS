from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        for word in words2:
            temp = Counter(word)
            for key in temp.keys():
                counter[key] = max(counter[key], temp[key])
        
        print(counter)

        res = []
        for word in words1:
            temp = Counter(word)
            check = True
            for key in counter.keys():
                if temp[key] < counter[key]:
                    check = False
                    break
            if check:
                res.append(word)

        return res