class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts = [-x for x in gifts]
        heapify(gifts)

        for _ in range(k):
            tar = -heappop(gifts)
            heappush(gifts, -math.isqrt(tar))

        return -sum(gifts)