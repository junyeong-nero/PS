class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        trie = dict()

        def add_trie(word):
            node = trie
            for c in word:
                if c not in node:
                    node[c] = dict()
                node = node[c]
            node["_check"] = word

        def find_smallest_root(word):
            node = trie
            for c in word:
                if "_check" in node:
                    return node["_check"]
                if c not in node:
                    return word
                node = node[c]
            return word

        for root in dictionary:
            add_trie(root)

        words = sentence.split()
        # print(words)

        words = [find_smallest_root(word) for word in words]
        # print(words)

        return " ".join(words)
