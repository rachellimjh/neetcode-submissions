class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix : number of times appeared
        prefixMap=defaultdict(int)
        prefixMap[0]=1
        res=0
        

        currSum=0

        for i,num in enumerate((nums)):
            currSum+=num
            diff=currSum-k
            if diff in prefixMap:
                res+=prefixMap[diff]
            prefixMap[currSum]=prefixMap.get(currSum,0)+1
        return res
        