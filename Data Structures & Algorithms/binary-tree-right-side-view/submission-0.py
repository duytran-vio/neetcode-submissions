class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return res