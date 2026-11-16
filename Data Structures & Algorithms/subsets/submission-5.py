class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]

        def dfs(i):
            if i == len(nums):
                res.append(cur[:])
                return
            # choice1 we take
            cur.append(nums[i])
            dfs(i+1)
            # choice2 we do not take
            cur.pop()
            dfs(i+1)
        
        dfs(0)
        return res
