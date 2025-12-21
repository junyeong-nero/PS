class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)

        d = defaultdict(list)
        for text, freq in counter.most_common():
            d[freq].append(text)
        for freq in d:
            d[freq] = sorted(d[freq])

        res = []
        for key in sorted(d.keys(), reverse=True):
            res += d[key]
            if len(res) >= k:
                break
        return res[:k]
