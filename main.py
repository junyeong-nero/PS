from typing import List
from itertools import accumulate
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush

arr = [1, 3, 3, 5, 7, 9] 
print(bisect_left(arr, 9))
print(bisect_right(arr, 9))