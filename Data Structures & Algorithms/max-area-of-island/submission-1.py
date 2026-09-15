class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        def dfs(r, c):
            if r < 0 or r == len(grid):
                return 0
            if c < 0 or c == len(grid[0]):
                return 0
            if (r, c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0
            
            visited.add((r, c))

            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curr_area = dfs(r, c)
                    max_area = max(max_area, curr_area)
        
        return max_area