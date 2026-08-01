class DSU:
    def __init__(self, n: int):
        self.size = [1] * n
        self.parent = list(range(n))

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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            if dsu.union(u, v):
                n -= 1

        return n