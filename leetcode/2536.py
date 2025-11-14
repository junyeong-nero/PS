class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        board = [[0] * n for _ in range(n)]
        def draw(query):
            x1, y1, x2, y2 = query
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    board[i][j] += 1
        

        for query in queries:
            draw(query)
    
        return board
            