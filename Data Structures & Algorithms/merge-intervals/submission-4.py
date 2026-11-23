class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res =[]
        intervals.sort()
        res.append(intervals[0])
        

        for start,end in intervals[1:]:
            if res[-1][1]>=start: # eg [1,3] [1,5] overlapping
                res[-1][0] = min(start,res[-1][0])
                res[-1][1] = max(res[-1][1],end)
            else:
                res.append([start,end])
        
        return res