class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # like BFS
        # explore ALL possible landing indices (neighbours)
        # pick best jump
        jumps=0
        current_end=0
        farthest=0

        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])

            if i == current_end:
                jumps+=1
                current_end=farthest # update end of the reachable range
        return jumps
