class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy way
        # reverse, try to shift goal to start
        goal=len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal: # if we can reach goal from i
                goal=i # shift goal to i
        
        return True if goal==0 else False