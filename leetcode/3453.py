class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        # binary search

        n = len(squares)
        squares = sorted(squares, key=lambda x: x[1])
        # print(squares)

        prefix = [0]
        # prefix[i] = sum(area[:i])
        for _, _, l in squares:
            prefix.append(prefix[-1] + l ** 2)
        

        total_area = prefix[-1] / 2
        # print(total_area)

        def func(y):
            area = 0

            # intersects
            i = j = bisect_left(squares, y, key=lambda x: x[1] + x[2])
            area = prefix[i]

            while j < n:
                if squares[j][1] < y < squares[j][1] + squares[j][2]:
                    area += (y - squares[j][1]) * squares[j][2]
                    j += 1
                else:
                    break
            # print(i, area)
            return area

        # print(func(0.5))
        temp = max(squares, key=lambda x: x[1] + x[2])
        left, right = 0, temp[1] + temp[2]

        while abs(left - right) > 10e-10:
            mid = (left + right) / 2
            area = func(mid)
            # print(left, right, mid, area)

            if area < total_area:
                left = mid
            else:
                right = mid
            
        return mid
        
