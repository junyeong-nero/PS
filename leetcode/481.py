class Solution:
    def magicalString(self, n: int) -> int:

        cur = "1"
        occurence = "1"

        def check(cur, occurence, delta):
            cur += delta
            occurence += str(len(delta))
            return occurence[-1] == cur[len(occurence) - 1]

        while len(cur) < n:
            if cur[-1] == "1":
                if check(cur, occurence, "2"):
                    cur += "2"
                    occurence += "1"
                    continue
                if check(cur, occurence, "22"):
                    cur += "22"
                    occurence += "2"
                    continue
            if cur[-1] == "2":
                if check(cur, occurence, "1"):
                    cur += "1"
                    occurence += "1"
                    continue
                if check(cur, occurence, "11"):
                    cur += "11"
                    occurence += "2"
                    continue

        return cur[:n].count("1")
