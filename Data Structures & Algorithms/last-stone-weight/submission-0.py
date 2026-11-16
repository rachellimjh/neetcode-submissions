class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap) # maxheap implementation in python
        # we use a minheap but store the negative values

        while len(heap)>1:
            first=heapq.heappop(heap)
            second=heapq.heappop(heap)

            # first=-8
            # second=-7
            if first!=second:
                heapq.heappush(heap,first-second)
            
        return -heap[0] if len(heap)==1 else 0


