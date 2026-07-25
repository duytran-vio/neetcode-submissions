class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], maxVal: int) -> int:
            if not node:
                return 0
            good_node_cnt = 1 if node.val >= maxVal else 0
            maxVal =  max(node.val, maxVal)
            good_node_cnt += dfs(node.left,maxVal)
            good_node_cnt += dfs(node.right, maxVal)
            return good_node_cnt

        return dfs(root, -1000)