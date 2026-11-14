class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area =0

        ROWS=len(grid)
        COLS=len(grid[0])

        seen=set()
        def dfs(i,j):
            if i<0 or i>=ROWS or j<0 or j>=COLS or grid[i][j]==0 or (i,j) in seen:
                return 0
            seen.add((i,j))
            return (1+dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1))
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1 and (i,j) not in seen:
                    area = max(dfs(i,j),area)
                    seen.add((i,j))
        
        return area