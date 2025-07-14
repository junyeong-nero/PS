class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:

        arr1, arr2 = arr1[::-1], arr2[::-1]
        n = max(len(arr1), len(arr2))

        arr1 += [0] * (n - len(arr1))
        arr2 += [0] * (n - len(arr2))
        # print(arr1, arr2)

        carry = 0
        res = []

        i = 0
        while i < n or carry != 0:
            temp = carry
            if i < n:
                temp = arr1[i] + arr2[i] + carry

            if temp == 3:
                temp = 1
                carry = -1
            elif temp == 2:
                temp = 0
                carry = -1
            elif temp == -1:
                temp = 1
                carry = 1
            else:
                carry = 0

            res.append(temp)
            i += 1

        # print(res[::-1])

        last_index = 0
        for i in range(len(res) - 1, -1, -1):
            if res[i] == 1:
                last_index = i
                break

        res = res[: last_index + 1]
        return res[::-1]
