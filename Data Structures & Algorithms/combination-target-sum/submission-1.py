class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]

        def dfs(i,total):
            if target==total: # possible combination
                res.append(cur[:])
                return
            if total>target or i>=len(nums):
                return
            cur.append(nums[i])
            dfs(i,total+nums[i])

            cur.pop()
            dfs(i+1,total) # skip this current num, so we move on

        dfs(0,0)

        return res