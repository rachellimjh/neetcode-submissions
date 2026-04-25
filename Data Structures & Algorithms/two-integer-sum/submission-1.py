class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        A = {}
        for i in range(len(nums)):
            diff=target-nums[i]
            if nums[i] in A:
                return [A[nums[i]],i]
            A[diff]=i
        