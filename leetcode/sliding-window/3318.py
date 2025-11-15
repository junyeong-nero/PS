class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def xsum(counter, x):
            arr = [(value, key) for key, value in counter.items()]
            arr = sorted(arr, reverse=True)
            return sum([value * key for value, key in arr[:x]])

        n = len(nums)
        counter = Counter(nums[0:k])
        res = [xsum(counter, x)]

        for i in range(k, n):
            counter[nums[i - k]] -= 1
            counter[nums[i]] += 1
            res.append(xsum(counter, x))
        
        return res


