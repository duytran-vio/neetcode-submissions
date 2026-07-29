class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        adj = {i : [] for i in range(numCourses)}
        for pre in prerequisites:
            degree[pre[0]] += 1
            adj[pre[1]].append(pre[0])

        q = []
        for course in range(numCourses):
            if degree[course] == 0:
                q.append(course)

        front = 0
        while front < len(q):
            u = q[front]
            for adj_node in adj[u]:
                degree[adj_node] -= 1
                if degree[adj_node] == 0:
                    q.append(adj_node)
            front += 1
        return q if len(q) == numCourses else []