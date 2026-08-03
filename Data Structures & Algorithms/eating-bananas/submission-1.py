class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        max_pile = max(piles)
        l, r = 1, max_pile

        min_k = max_pile

        while l <= r:
            k = l + (r - l) // 2
            time = 0
            
            for pile in piles:
                time += math.ceil(pile / k)
            if time <= h:
                r = k - 1
                min_k = min(k, min_k)
            elif time > h:
                l = k + 1

        return min_k