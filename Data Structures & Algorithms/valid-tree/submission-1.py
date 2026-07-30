class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = [False] * n
        def dfs(node, par) -> bool:
            if visited[node]:
                return False
            visited[node] = True
            for neigh in adj[node]:
                if neigh == par:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        for isVisited in visited:
            if not isVisited:
                return False
        return True