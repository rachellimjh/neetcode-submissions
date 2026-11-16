class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # 2 cases:
        # 1. k<len(nums): pop from heap
        # 2. k>len(nums): do not pop from heap
        self.k=k
        self.minHeap=nums
        heapq.heapify(self.minHeap)
        while self.k<len(self.minHeap):
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        if self.k<len(self.minHeap):
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        