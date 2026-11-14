class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        path=[]
        def backtracking(i): # i is index
            if i==len(nums):
                res.append(path[:]) # save the result at leaf
                return
            
            # choice 1 to take the element
            path.append(nums[i])
            backtracking(i+1)
            
            # choice 2 do not take elemt
            path.pop()
            backtracking(i+1)
        backtracking(0)
        return res