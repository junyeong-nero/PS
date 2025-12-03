class Solution:
    def magicalString(self, n: int) -> int:
        # "1" -> "1"
        def is_magical(s):
            m = len(s)
            i = 0
            converted = ""
            while i < m:
                j = i + 1
                while j < m and s[i] == s[j]:
                    j += 1
                converted += str(j - i)
                i = j
            return converted == s[: len(converted)]

        cur = "1"
        size = 1
        res = 1

        while size < n:
            if is_magical(cur + "1"):
                cur += "1"
                res += 1
                size += 1
            elif is_magical(cur + "11"):
                cur += "11"
                res += 2
                size += 2
            elif is_magical(cur + "2"):
                cur += "2"
                size += 1
            elif is_magical(cur + "22"):
                cur += "22"
                size += 2
            else:
                return -1

        return cur[:n].count("1")
