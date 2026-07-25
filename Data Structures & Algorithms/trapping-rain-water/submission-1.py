class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0

        for level in range(1, max(height)+1):
            blocks = []
            for position in range(len(height)):
                if height[position] >= level:
                    blocks.append(position)

            left_boundary, right_boundary = min(blocks), max(blocks)

            for position in range(len(height)):
                if height[position] < level:
                    if position > left_boundary and position < right_boundary:
                        trapped_water += 1
            
        return trapped_water