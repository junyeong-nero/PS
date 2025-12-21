class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:

        def check(index):
            if not isActive[index]:
                return False
            for char in code[index]:
                if char.isnumeric() or char.isalpha() or char == "_":
                    continue
                return False

            if businessLine[index] not in [
                "electronics",
                "grocery",
                "pharmacy",
                "restaurant",
            ]:
                return False

            return True

        n = len(code)
        res = [(businessLine[i], code[i]) for i in range(n) if check(i) and code[i]]
        res = sorted(res)
        res = [code_ for category, code_ in res]

        return res
