class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 1. sort so duplicates are adjacent
        res, cur = [], []

        def dfs(i,cur,total):
            if total==target:
                res.append(cur[:])
                return 
            if i>=len(candidates) or total>target:
                return
            
            # include candidate
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            cur.pop()

            # exclude candidate
            while i+1<len(candidates) and candidates[i]==candidates[i+1] :
                i+=1
            dfs(i+1,cur,total)
        dfs(0,[],0)
    
        return res