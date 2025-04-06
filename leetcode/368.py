class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        n = len(nums)
        d = defaultdict(list)

        for num in nums:
            temp = []
            # fine longest subset ends with nums
            for key, value in d.items():
                if num % key == 0 and len(temp) < len(value):
                    temp = value[:]
            temp.append(num)
            d[num] = temp

        ans = max(d.values(), key=len)
        return ans
