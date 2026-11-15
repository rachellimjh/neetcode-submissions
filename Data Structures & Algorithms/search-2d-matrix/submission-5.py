class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS=len(matrix)
        COLS=len(matrix[0])

        l,r=0,(ROWS*COLS-1)

        while l<=r:
            m=l+(r-l)//2

            row=m//COLS
            col=m%COLS
            if matrix[row][col]==target:
                return True
            if matrix[row][col]<target:
                l+=1
            else:
                r-=1

        return False 
