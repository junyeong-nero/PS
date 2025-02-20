class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set([int(x, 2) for x in nums])
        n = len(nums[0])
        # print(s)

        i = 0
        while True:
            if i not in s:
                return str(bin(i))[2:].rjust(n, '0')
            i += 1
        
        return ''