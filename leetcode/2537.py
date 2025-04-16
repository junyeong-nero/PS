class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = Counter()
        n = len(nums)
        i = j = 0
        res = 0
        while j < n and i <= j:
            counter[nums[j]] += 1
            temp = sum([value * (value - 1) // 2 for value in counter.values()])
            print(i, j, temp)
            
            if temp < k:
                j += 1
            else:
                # res += (i + 1) * (n - j)
                res += (n - j)
                counter[nums[i]] -= 1
                i += 1
                if j < n - 1:
                    j += 1
        
        return res