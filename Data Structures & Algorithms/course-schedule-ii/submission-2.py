class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree=[0]*numCourses
        graph=defaultdict(list)

        for course,pre in prerequisites:
            graph[pre].append(course)
            in_degree[course]+=1
        
        q = deque(i for i in range(numCourses) if in_degree[i]==0)
        order=[]

        while q:
            node=q.popleft()
            order.append(node)
            for nei in graph[node]:
                in_degree[nei]-=1
                if in_degree[nei]==0:
                    q.append(nei)

        return order if len(order)==numCourses else []
