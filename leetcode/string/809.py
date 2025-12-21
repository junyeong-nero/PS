class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def get_info(arr):
            counter = []
            n = len(arr)
            i = 0
            while i < n:
                j = i + 1
                while j < n and arr[i] == arr[j]:
                    j += 1
                counter.append((arr[i], j - i))
                i = j
            return counter

        def check(ref, cand):
            if len(ref) != len(cand):
                return False

            n = len(ref)
            for i in range(n):
                if ref[i][0] != cand[i][0]:
                    return False
                if ref[i][1] != cand[i][1]:
                    if ref[i][1] < cand[i][1]:
                        return False
                    if ref[i][1] < 3:
                        return False

            return True

        res = 0
        info = get_info(s)
        for word in words:
            if check(info, get_info(word)):
                res += 1

        return res
