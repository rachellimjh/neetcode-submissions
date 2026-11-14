class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])

        seen=set()
        count=0
        def dfs(i,j):
            if i<0 or i>=(ROWS) or j<0 or j>=(COLS) or (i,j) in seen or grid[i][j]=="0":
                return
            seen.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1" and (i,j) not in seen:
                    dfs(i,j)
                    count+=1

        return count