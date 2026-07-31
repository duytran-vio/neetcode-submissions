class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode) -> tuple[int, int, bool]:
            if node.left == None and node.right == None:
                return node.val, node.val, True
            max = min = node.val
            if node.left:
                maxL, minL, isLeftBST = dfs(node.left)
                if not isLeftBST or maxL >= node.val:
                    return 0, 0, False
                min = minL

            if node.right:
                maxR, minR, isRightBST = dfs(node.right)
                if not isRightBST or minR <= node.val:
                    return 0, 0, False
                max = maxR

            return max, min, True

        _, _, isBST = dfs(root)
        return isBST