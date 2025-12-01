class Solution:
    def originalDigits(self, s: str) -> str:

        order = [
            ("z", "zero", "0"),
            ("w", "two", "2"),
            ("u", "four", "4"),
            ("x", "six", "6"),
            ("g", "eight", "8"),
            ("o", "one", "1"),
            ("f", "five", "5"),
            ("v", "seven", "7"),
            ("i", "nine", "9"),
            ("t", "three", "3"),
        ]

        res = ""
        counter = Counter(s)

        for key, value, num_str in order:
            if counter[key] == 0:
                continue

            res += num_str * counter[key]
            counter -= Counter(value * counter[key])

        res = "".join(sorted(list(res)))
        return res
