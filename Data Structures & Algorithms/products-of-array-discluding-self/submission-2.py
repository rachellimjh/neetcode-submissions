class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of all nums after i: suffix
        # product of all nums before i: prefix

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        return [prefix[i] * suffix[i] for i in range(len(nums))]