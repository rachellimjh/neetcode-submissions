class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        
        ans=[]
        most_common = count.most_common()
        for i in range(k):
            ans.append(most_common[i][0])

        return ans