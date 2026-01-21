class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        # ans[i] | ans[i] + 1 == nums[i]
        # minimize(ans[i]) !
        # nums[i] = 10001111
        # ans[i] =  10000111

        # nums[i] = 101010
        # ans[i] =  101001

        # nums[i] = 101000
        # ans[i] =  10X000

        # 111 | 10111 | 101 | 1100001
        # 011 | 10011 | 100 | 1100000

        def func(num):
            if num % 2 == 0:
                return -1

            mask, count = 0, 0
            while num & 1 == 1:
                # print(bin(num), bin(mask))
                if count > 0:
                    mask |= 1 << (count - 1)
                num >>= 1
                count += 1

            mask |= num << count
            # print(bin(mask))
            return mask

        res = []
        for num in nums:
            # print(num)
            res.append(func(num))

        return res
