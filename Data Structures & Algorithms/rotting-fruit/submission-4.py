class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])

        fresh=0
        time=0
        q=deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        
        directions=[[0,1],[0,-1],[-1,0],[1,0]]

        while q and fresh>0:
            for i in range(len(q)): # to separate by levels of the tree
                r,c=q.popleft()
                for dr,dc in directions:
                    row=dr+r
                    col=dc+c
                    if 0<=row<ROWS and 0<=col<COLS and grid[row][col]==1:
                        grid[row][col]=2
                        fresh-=1
                        q.append((row,col))
        
            time+=1

        return time if fresh==0 else -1