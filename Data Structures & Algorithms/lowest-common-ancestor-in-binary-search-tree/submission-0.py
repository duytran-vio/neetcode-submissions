
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = self.dfs(root, p, q)
        return lca
       
    def dfs(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left_lca = self.lowestCommonAncestor(root.left, p, q) 
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        if left_lca and right_lca:
            return root
        if not left_lca and not right_lca:
            return None
        return left_lca if left_lca else right_lca