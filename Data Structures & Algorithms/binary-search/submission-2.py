class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # usually O(logn) solutions are binary search, much better than O(n)
        # sorted array to look for target
        # try to implement it quickly 

        l,r=0,len(nums)-1
        while l<=r: # the pointers can be equal, it means we havent looked at those values yet
            m = l+((r-l) // 2) # l+r might lead to overflow
            if nums[m]>target:
                r = m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m
        return -1
