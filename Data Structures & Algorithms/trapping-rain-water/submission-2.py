class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0

        l, r = 0, len(height) - 1
        l_max = r_max = 0
        while l < r:
            if height[l] < height[r]:
                l_max = max(height[l], l_max)
                water = l_max - height[l]
                trapped_water += water
                l += 1
            else:
                r_max = max(height[r], r_max)
                water = r_max - height[r]
                trapped_water += water
                r -= 1
        
        return trapped_water