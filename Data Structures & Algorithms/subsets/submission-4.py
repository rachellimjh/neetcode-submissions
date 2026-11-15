class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path=[]

        def dfs(i,path):
            if i==len(nums):
                res.append(path[:])
                return
            
            
            # choice 1: take current num
            path.append(nums[i])
            dfs(i+1,path)
            # choice 2: do not take current num
            path.pop()
            dfs(i+1,path)

        dfs(0,path)
        return res