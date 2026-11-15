class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        currSum=0

        for n in nums:
            if currSum<0:
                currSum=0
            currSum+=n # this is the key, for if negatives only array
            maxSub=max(maxSub,currSum)
        return maxSub