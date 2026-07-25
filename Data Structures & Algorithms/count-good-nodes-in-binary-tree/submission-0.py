class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        good_node_cnt = 0
        def dfs(node: Optional[TreeNode], stack: List[TreeNode], good_node_cnt: int) -> int:
            if not node:
                return good_node_cnt
            if len(stack) == 0 or stack[-1].val <= node.val:
                stack.append(node)
                good_node_cnt = good_node_cnt + 1

            good_node_cnt = dfs(node.left, stack, good_node_cnt)
            good_node_cnt = dfs(node.right, stack, good_node_cnt)
            if len(stack) > 1 and stack[-1] == node:
                stack.pop()
            return good_node_cnt

        good_node_cnt = dfs(root, stack, good_node_cnt)
        return good_node_cnt