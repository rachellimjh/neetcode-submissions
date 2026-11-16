"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap=[] # minHeap of ending time currently in use
        
        for interval in intervals:
            start,end=interval.start,interval.end

            if heap and heap[0]<=start: # if meeting start at 15, meeting in room end 10, we can REuse the room. SHARE THE ROOM
                heapq.heappop(heap)
            heapq.heappush(heap,end)
        return len(heap)



        
