class Solution:
        # O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights.append(0)
        
        res = 0
        for right in range(1,len(heights)):
            while stack and heights[stack[-1]] > heights[right]:
                h = heights[stack.pop()]
                left = -1 if not stack else stack[-1] # because pop operation, left = stack.pop() is not the left boundary
                w = right - left -1
                res = max(res,h*w)
            stack.append(right)
        return res
    
    # O(n2)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        heights = [0]*len(matrix[0])
        res = 0
        for row in matrix:
            for i in range(len(row)):
                heights[i] = heights[i] + int(row[i]) if int(row[i]) else 0
            res = max(res,self.largestRectangleArea(heights))
        return res