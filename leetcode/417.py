class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        po = [[False] * n for _ in range(m)]
        ao = [[False] * n for _ in range(m)]
        for i in range(m):
            po[i][0] = True
            ao[i][-1] = True

        for j in range(n):
            po[0][j] = True
            ao[-1][j] = True

        for x in range(1, m):
            for y in range(1, n):
                if heights[x][y] >= heights[x - 1][y]:
                    po[x][y] |=  po[x - 1][y]
                if heights[x][y] >= heights[x][y - 1]:
                    po[x][y] |=  po[x][y - 1]
        
        for x in range(m - 2, -1, -1):
            for y in range(n - 2, -1, -1):
                if heights[x][y] >= heights[x + 1][y]:
                    ao[x][y] |=  ao[x + 1][y]
                if heights[x][y] >= heights[x][y + 1]:
                    ao[x][y] |=  ao[x][y + 1]

        print(po)
        print(ao)

        res = []
        for x in range(m):
            for y in range(n):
                if ao[x][y] and po[x][y]:
                    res.append([x, y])

        return res