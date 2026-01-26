@cache
def is_prime(n):
    """
    Checks if a number n is prime.
    """
    if n < 2:
        return False  # Numbers less than 2 are not prime.
    if n == 2:
        return True  # 2 is the only even prime number.
    if n % 2 == 0:
        return False  # Other even numbers are not prime.

    # Check for odd divisors up to the square root of n.
    max_divisor = int(math.sqrt(n)) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False

    return True


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        # p < nums[i]
        # nums[i] -= p

        # index 당 한 번 만 가능...

        def reachable(k, lower_bound=0):
            # k - x > lowerbound
            # k - lowerbound > x
            for x in range(min(k - 1, k - lower_bound - 1), 0, -1):
                if is_prime(x):
                    return k - x
            return k

        last = 0
        for num in nums:
            cur = reachable(num, last)
            # print(cur)
            if cur <= last:
                return False
            last = cur

        return True
