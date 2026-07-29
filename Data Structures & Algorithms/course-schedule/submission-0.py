class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        adj = {}
        for pre in prerequisites:
            degree[pre[1]] += 1
            if pre[0] not in adj:
                adj[pre[0]] = []
            adj[pre[0]].append(pre[1])

        q = deque([])
        cnt = 0
        for course in range(numCourses):
            if degree[course] == 0:
                q.append(course)
                cnt += 1

        while q:
            u = q.pop()
            for adj_node in adj.get(u, []):
                degree[adj_node] -= 1
                if degree[adj_node] == 0:
                    q.append(adj_node)
                    cnt += 1
        return True if cnt == numCourses else False