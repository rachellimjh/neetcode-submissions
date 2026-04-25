class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = []

        for i in range(1,len(nums)):
            prefix[i]=nums[i-1]*prefix[i-1]
        
        for j in range(n-2,-1,-1):
            suffix[j]=suffix[j+1]*nums[j+1]
        
        for i in range (len(nums)):
            ans=prefix[i]*suffix[i]
            res.append(ans)
        return res