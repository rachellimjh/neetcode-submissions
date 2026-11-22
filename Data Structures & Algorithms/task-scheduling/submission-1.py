class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # key intuition: do the most frequent task first
        # use maxHeap to keep track of most frequent task
        # pop it to do task

        # queue: (count, time we can process task agn=n+time[now])

        count=Counter(tasks)
        maxHeap=[-c for c in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time=0

        while maxHeap or q:
            if maxHeap:
                count=heapq.heappop(maxHeap)
                count+=1 # since we are storing negative
                if count!=0:
                    q.append([count, time+n])

            if q and time==q[0][1]:
                heapq.heappush(maxHeap,q.popleft()[0])
            time+=1
        return time