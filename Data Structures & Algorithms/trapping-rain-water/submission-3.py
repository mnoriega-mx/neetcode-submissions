class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        trapped_water = 0

        max_left = height[0]
        max_right = height[-1]
        while l < r:
            max_border = min(max_left, max_right)
            if height[l] < height[r]:
                trapped_water += max_border - height[l]
                l += 1
                max_left = max(height[l], max_left)
            else:
                trapped_water += max_border - height[r]
                r -= 1
                max_right = max(height[r], max_right)
        
        return trapped_water