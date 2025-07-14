class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        # print(words)

        tree = dict()

        def add(tree, word):
            cur = tree
            check = True
            for char in word[:-1]:
                if char not in cur:
                    check = False
                    break
                cur = cur[char]

            if check:
                cur[word[-1]] = dict()
                return len(word)

            return 0

        res = ""
        for word in words:
            size = add(tree, word)
            if size > len(res):
                res = word

        # print(tree)
        return res
