class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses = sorted(houses)
        heaters = sorted(heaters)
        n = len(heaters)

        def check(radius):
            for house in houses:
                i = bisect_left(heaters, house)
                j = i - 1
                if 0 <= i < n and heaters[i] - house <= radius:
                    continue
                if 0 <= j < n and house - heaters[j] <= radius:
                    continue
                return False
            return True

        i = 0
        j = max(houses + heaters)

        while i <= j:
            mid = (i + j) // 2
            temp = check(mid)
            if not temp:
                i = mid + 1
            else:
                j = mid - 1

        return i
