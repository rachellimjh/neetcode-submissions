class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=0

        l,r=0,len(nums)-1
        
        while l<r:
            m=l+(r-l)//2
            
            if nums[m]>nums[r]: # eg [2,3,4,5,1]
                l=m+1
            else:
                r=m # need to include m because it can be at m
        
        return nums[r]