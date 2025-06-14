from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points):
        res = 0
        
        for i in points:
            distance_map = defaultdict(int)
            
            for j in points:
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                dist_sq = dx * dx + dy * dy
                distance_map[dist_sq] += 1
            
            for count in distance_map.values():
                if count >= 2:
                    res += count * (count - 1)
        
        return res