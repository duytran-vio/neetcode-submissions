class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        iPos = {}
        for i, iNode in enumerate(inorder):
            iPos[iNode] = i

        def dfs(pNode, pStart, pEnd, iStart, iEnd) -> TreeNode:
            nodeVal = preorder[pNode]
            iNode = iPos[nodeVal]
            node = TreeNode(nodeVal)
            leftNodeCount = iNode - iStart 

            if iStart < iNode:
                leftNode = dfs(pNode + 1, pNode + 1, pNode + leftNodeCount, iStart, iNode - 1)
                node.left = leftNode

            if iNode < iEnd:
                pRightStart = pNode + leftNodeCount + 1
                rightNode = dfs(pRightStart, pRightStart, pEnd, iNode + 1, iEnd)
                node.right= rightNode
            return node
        return dfs(0, 0, len(preorder) - 1, 0, len(inorder) - 1)
            