class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(heights)
        max_value = max(heights)
        d = defaultdict(list)
        for i, v in enumerate(heights):
            d[v].append(i)
        
        keys = sorted(d.keys())
        
        def help(query):
            a, b = query
            start, end = max(a, b), min(a, b)
            if max_value == heights[start]:
                return start
            if heights[start] > heights[end] or start == end:
                return start

            i = bisect_right(keys, max(heights[a], heights[b]))
            res = n
            while i < len(keys):
                key = keys[i]
                j = bisect_right(d[key], start)
                if j < len(d[key]) and d[key][j] > start:
                    res = min(res, d[key][j])
                i += 1
            return res if res < n else -1
    
        return [help(q) for q in queries]