class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        size = {}
        def countSize(node: Optional[TreeNode], size):
            if node is None:
                return 0
            sizeL = countSize(node.left, size)
            sizeR = countSize(node.right, size)
            size[node] = sizeL + sizeR + 1
            return size[node]

        countSize(root, size)

        def findKth(node: Optional[TreeNode], k: int) -> int:
            if node is None:
                return 0
            sizeL = 0
            if node.left:
                sizeL = size[node.left]

            if k == sizeL + 1:
                return node.val
            elif k <= sizeL:
                return findKth(node.left, k)
            else:
                return findKth(node.right, k - sizeL - 1)
        return findKth(root, k)