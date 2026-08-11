class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        l = r = 0

        for i in range(n):
            if i < r:
                p[i] = min(r - i, p[l + r - i])
            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            if i + p[i] > r:
                r = i + p[i]
                l = i - p[i]

        total = 0
        for i in range(n):
            total += (p[i] if t[i] == '#' else p[i] + 1) // 2
        return total