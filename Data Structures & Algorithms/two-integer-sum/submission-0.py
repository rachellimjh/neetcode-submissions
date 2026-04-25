class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        for i in range(len(nums)):
            diff=target-nums[i]
            if nums[i] in difference:
                return[difference[nums[i]],i]

            difference[diff]=i