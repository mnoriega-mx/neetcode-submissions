class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def dfs(r, c):
            if r == len(grid) or r < 0:
                return
            if c == len(grid[0]) or c < 0:
                return
            if (r, c) in visited:
                return
                
            block = grid[r][c]
            if block == '0':
                return
            else:
                visited.add((r, c))
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands
