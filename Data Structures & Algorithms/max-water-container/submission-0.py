class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        biggest_container = 0

        while left < right:
            length = right - left
            height = min(heights[left], heights[right])

            current_capacity = length * height

            biggest_container = max(biggest_container, current_capacity)

            if heights[left] < heights[right]:
                while heights[left + 1] < heights[left]:
                    left += 1
                left += 1
            else:
                while heights[right - 1] < heights[right]:
                    right -= 1
                right -= 1
        
        return biggest_container