class Solution:
    def maxDiff(self, num: int) -> int:

        def find_target(s, ignore=[]):
            for c in s:
                if c in ignore:
                    continue
                return c
            return ignore[0]

        num = str(num)
        target_min = find_target(num, [num[0], "0"])
        target_max = find_target(num, ["9"])

        max_value = int(num.replace(target_max, "9"))
        if num[0] == "1" and target_min != "1":
            min_value = int(num.replace(target_min, "0"))
        else:
            min_value = int(num.replace(num[0], "1"))

        # print(max_value, min_value)
        return max_value - min_value
