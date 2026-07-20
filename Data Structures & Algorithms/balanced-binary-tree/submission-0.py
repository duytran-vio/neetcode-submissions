class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [root]
        mp : dict[Optional[TreeNode], int] = {None: 0}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight = mp[node.left]
                rightHeight = mp[node.right]

                if abs(leftHeight - rightHeight) > 1:
                    return False 
                mp[node] = max(leftHeight, rightHeight) + 1
        return True