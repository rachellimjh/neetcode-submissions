class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        
        curr=[]
        def dfs(i,curr):
            if i==len(nums):
                res.append(curr[:])
                return
            
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()
            dfs(i+1,curr)

        dfs(0,curr)
        return res


        # choice 1: take current element

        # choice 2: do not take it