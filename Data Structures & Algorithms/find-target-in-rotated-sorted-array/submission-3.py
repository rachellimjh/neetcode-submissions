class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # since sorted: we can think of binary search

        l=0
        r=len(nums)-1

        while l<=r:
            m = l+(r-l)//2
            if nums[m]==target:
                return m

            # if left half is sorted
            if nums[l] <= nums[m]:
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l=m+1
                
            # if right half is sorted
            else:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        
        return -1


