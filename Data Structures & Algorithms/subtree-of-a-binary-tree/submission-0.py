
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def toString(node: Optional[TreeNode]) -> str:
            if not node:
                return "$#"
            return "$" + str(node.val) + toString(node.left) + toString(node.right)

        root_str = toString(root)
        subroot_str = toString(subRoot)

        def isContain(s: str, st: str) -> bool:
            sub_len = len(st)
            s = st + "|" + s
            l, r, z, n = 0, 0, [0] * len(s), len(s)
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[i + z[i]] == s[z[i]]:
                    z[i] += 1

                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1

                if z[i] == sub_len:
                    return True
            return False

        return isContain(root_str, subroot_str)