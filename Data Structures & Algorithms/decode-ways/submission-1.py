class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        def isValidForDecode(st: str) -> bool:
            if st[0] == '0':
                return False
            value = int(st)
            return 1 <= value and value <= 26
        
        d = [0] * (n + 1)
        d[0] = 1
        d[1] = isValidForDecode(s[0]) * d[0]
        for i in range(2, n + 1):
            d[i] += d[i - 1] * isValidForDecode(s[i - 1]) + d[i - 2] * isValidForDecode(s[i - 2: i])
        return d[n]