class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]

        for i, (start,end) in enumerate(intervals):

            # new interval goes AFTER current eg [1,2] [3,4]
            if end<newInterval[0]:
                res.append([start,end])
                
            # new interval goes BEFORE current 
            elif newInterval[1]<start:
                res.append(newInterval)
                res.extend(intervals[i:]) # rest of intervals
                return res
            # merge
            else: # eg [1,2][2,5]
                mergedstart=min(start,newInterval[0])
                mergedend=max(end,newInterval[1])
                newInterval=[mergedstart,mergedend]
            
        res.append(newInterval)
        return res