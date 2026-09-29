class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[] for _ in range(n + 1)]

        dp = [[False] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    if j + 1 >= i - 1 or dp[j + 1][i - 1]:
                        dp[j][i] = True

        f[0] = [[]]
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                substr = s[j: i]
                if dp[j][i - 1]:
                    tmp = []
                    for e in f[j]:
                        tmp.append(e.copy())
                    for e in tmp:
                        e.append(substr)
                    f[i].extend(tmp)
        return f[n]