class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d = {}
        for num in sorted(nums)[::-1]:
            if num**2 in d and num in d and num != 1:
                d[num] = d[num**2] + 2
            else:
                d[num] = 1
        ones = nums.count(1)
        return max(max(d.values()), ones - (ones % 2 == 0))


# class Solution:
#     def maximumLength(self, nums: List[int]) -> int:

#         # prime-factorization(num) -> counter
#         # O(N^2)

#         # using logs
#         counter = Counter(nums)

#         def check_base(base):
#             base_counter = dict()
#             for key, value in counter.items():
#                 temp = log(key, base)
#                 if int(temp) - temp < 10e-7:
#                     base_counter[temp] = value

#             index = 1
#             count = 0
#             while base_counter.get(index, 1) >= 2:
#                 index *= 2
#                 count += 2

#             if index in base_counter:
#                 return count + 1
#             return count - 1

#         res = 1

#         temp = nums.count(1)
#         res = max(res, temp - 1 if temp % 2 == 0 else temp)

#         for key in counter:
#             if key == 1:
#                 continue
#             # print(key, check_base(key))
#             res = max(res, check_base(key))

#         return res
