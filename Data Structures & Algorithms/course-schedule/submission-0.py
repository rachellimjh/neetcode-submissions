class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree=[0]*(numCourses)
        graph=defaultdict(list)

        # build adjacency list and indegree count
        for course,pre in prerequisites:
            graph[pre].append(course)
            in_degree[course]+=1
        
        # we can visit those without in edges, meaning no dependencies 
        q = deque(i for i in range(numCourses) if in_degree[i]==0)
        taken=0

        while q:
            node=q.popleft() # taking this course now
            taken+=1
            for nei in graph[node]:
                in_degree[nei]-=1
                if in_degree[nei]==0:
                    q.append(nei)

        return taken==numCourses
