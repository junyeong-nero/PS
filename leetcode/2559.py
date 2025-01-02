from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        vowels = "aeiou"
        
        for word in words:
            temp = prefix[-1]
            if word[0] in vowels and word[-1] in vowels:
                temp += 1
            prefix.append(temp)
