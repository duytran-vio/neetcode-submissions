class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        l = r = center = 0
        m = [0] * len(t)
        for i in range(len(t)):
            if i < r:
                m[i] = min(r - i, m[l+(r-i)])

            while i + m[i] + 1 < len(t) and i - m[i] - 1 >= 0 and t[i + m[i] + 1] == t[i - m[i] - 1]:
                m[i] += 1

            if i + m[i] > r:
                center = i
                l = i - m[i]
                r = i + m[i]

        resL, center_idx = max((v, i) for i, v in enumerate(m))
        start = (center_idx - resL) // 2
        return s[start: start + resL]