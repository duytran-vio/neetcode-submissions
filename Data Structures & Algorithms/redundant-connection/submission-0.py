class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node: int):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u: int, v: int) -> bool:
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u, v in edges:
            if not dsu.union(u - 1, v - 1):
                return [u, v]
        return []