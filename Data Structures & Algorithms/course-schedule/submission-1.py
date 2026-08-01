from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque([c for c in range(numCourses) if indegree[c] == 0])
        taken = 0

        while q:
            node = q.popleft()
            taken += 1

            for next in graph[node]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)

        return taken == numCourses
            


        