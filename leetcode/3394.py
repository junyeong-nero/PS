class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        def check_overlap(arr):
            arr = sorted(arr)
            prev = n + 1
            res = 0
            for i in range(len(arr)):
                if prev <= arr[i][0]:
                    res += (arr[i][0] - prev + 1)
                prev = arr[i][1]

            return res

        V = [(rect[0], rect[2]) for rect in rectangles]
        H = [(rect[1], rect[3]) for rect in rectangles]

        return check_overlap(V) >= 2 or check_overlap(H) >= 2

