from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        i = res = 0

        while i < n:
            a, b = set(), set()

            for j in range(i, n):
                a.add(arr[j])
                b.add(j)

                if a == b:
                    res += 1
                    i = j + 1
                    break
            else:
                # If no break occurs, exit the loop
                break

        return res
