class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # usually O(logn) solutions are binary search, much better than O(n)
        # sorted array to look for target
        # try to implement it quickly 
        # idea is to cut search by half each time
        l,r=0,len(nums)-1

        while l<=r:
            m=(l+r)//2 #find the middle index
            if target<nums[m]:
                r=m-1
            elif target>nums[m]:
                l=m+1
            else:
                return m
        return -1
                