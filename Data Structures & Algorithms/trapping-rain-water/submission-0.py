class Solution:
    def trap(self, height: List[int]) -> int:
        grid = []
        trapped_water = 0

        for i in range(max(height)):
            grid.append([0] * len(height))

        for level in range(len(grid)):
            for block in range(len(grid[level])):
                if height[block] >= level + 1:
                    grid[level][block] = 1

        for level in range(len(grid)):
            blocks = []
            for block in range(len(grid[level])):
                if grid[level][block] == 1:
                    blocks.append(block)
            
            left, right = min(blocks), max(blocks)

            water = 0
            for block in range(len(grid[level])):
                if grid[level][block] == 1:
                    continue
                if block > left and block < right:
                    water += 1
            trapped_water += water

        return trapped_water