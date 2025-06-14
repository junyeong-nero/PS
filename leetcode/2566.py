class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        num = str(num)
        target = "9"
        for c in num:
            if c == "9":
                continue
            else:
                target = c
                break
        # print(target)

        max_value = int(num.replace(target, "9"))
        min_value = int(num.replace(num[0], "0"))
        # print(max_value, min_value)

        res = max_value - min_value
        return res