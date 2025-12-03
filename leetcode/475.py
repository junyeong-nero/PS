import bisect


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        n = len(houses)
        m = len(heaters)

        heaters.sort()
        ans = 0

        for house in houses:
            index = bisect.bisect_left(heaters, house)
            if index == 0:
                distance = heaters[0] - house
            elif index == m:
                distance = house - heaters[-1]
            else:
                distance = min(heaters[index] - house, house - heaters[index - 1])
            ans = max(ans, distance)

        return ans
