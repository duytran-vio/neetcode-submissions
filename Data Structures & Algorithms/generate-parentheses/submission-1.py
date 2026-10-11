class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr, open, close):
            if open == close == n:
                res.append("".join(curr))
                return
            if open < n:
                curr.append('(')
                dfs(curr, open + 1, close)
                curr.pop()
            if close < open:
                curr.append(')')
                dfs(curr, open, close + 1)
                curr.pop()
            return
        dfs([], 0, 0)
        return res