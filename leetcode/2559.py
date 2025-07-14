class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        vowel = "aeiou"
        for word in words:
            temp = prefix[-1]
            if word[0] in vowel and word[-1] in vowel:
                temp += 1
            prefix.append(temp)

        # print(prefix)
        # prefix[i] : # of vowels in words[:i]
        return [prefix[r + 1] - prefix[l] for l, r in queries]
