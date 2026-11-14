class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        
        curr=[]
        def dfs(i,curr):
            if i==len(nums):
                res.append(curr[:])
                return
            
            # choice 1: take current element
            curr.append(nums[i])
            dfs(i+1,curr)
            # choice 2: do not take it
            curr.pop()
            dfs(i+1,curr)

        dfs(0,curr)
        return res
