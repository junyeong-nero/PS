class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        single_digit = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }

        double_digit = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        digit = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }

        def num_to_words(num):
            res = []
            hundred = num // 100
            if hundred > 0:
                res += [single_digit[hundred], "Hundred"]

            left = num % 100
            if left in single_digit:
                res += [single_digit[left]]
            elif left in double_digit:
                res += [double_digit[left]]
            else:
                a = left // 10
                b = left % 10
                temp = []
                if a > 0:
                    temp.append(digit[a])
                if b > 0:
                    temp.append(single_digit[b])
                res += temp

            return res

        res = []
        postfix = ["", "Thousand", "Million", "Billion", "Trillion"]
        index = 0
        while num > 0:
            temp = num_to_words(num % 1000)
            if index > 0 and num % 1000 > 0:
                temp += [postfix[index]]
            res = temp + res
            num //= 1000
            index += 1

        # print(res)
        return " ".join(res).strip()
