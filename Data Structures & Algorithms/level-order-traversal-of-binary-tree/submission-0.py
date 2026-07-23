
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)])
        res : List[List[TreeNode]] = []

        while q:
            node, level = q.popleft()
            if len(res) == level:
                res.append([])
            res[level].append(node)

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return [[node.val for node in nodes] for nodes in res]
        