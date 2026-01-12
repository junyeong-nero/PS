class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        temp = [(abs(elem - x), elem) for elem in arr]
        temp = sorted(temp)

        # print(temp)
        return sorted([elem[1] for elem in temp[:k]])
