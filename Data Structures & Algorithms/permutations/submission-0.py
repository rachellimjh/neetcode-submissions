class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        if len(nums)==0: # base case
            return [[]]
        
        perms=self.permute(nums[1:]) # recursion is to just remove 1st element
        for p in perms:
            for i in range(len(p)+1): # try slotting it in diff postions
                p_copy=p.copy()
                p_copy.insert(i,nums[0]) # first element
                res.append(p_copy)
        return res