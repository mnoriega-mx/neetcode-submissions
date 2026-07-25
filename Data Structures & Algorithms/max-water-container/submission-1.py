class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_water = 0
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])

            water = width * height
            max_water = max(water, max_water)

            if heights[l] < heights[r]:
                while heights[l+1] < heights[l]:
                    l += 1
                l += 1
            else:
                while heights[r-1] < heights[r]:
                    r -= 1
                r -= 1
            
        return max_water