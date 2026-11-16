class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap=[]
        for x,y in points:
            dist=x**2+y**2
            minHeap.append([dist,x,y]) 
            # create list first
        
        # after list created
        # heapify takes first element as primary key
        # so it will sort by it
        heapq.heapify(minHeap)
        res=[]
        while k>0:
            dist,x,y=heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res