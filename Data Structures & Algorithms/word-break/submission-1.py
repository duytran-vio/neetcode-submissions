class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) 
        f = [False] * (n + 1)
        f[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                if self.is_suffix(s[:i], w):
                    f[i] |= f[i - len(w)]
        return f[n]
    def is_suffix(self, s, st):
        if len(s) < len(st):
            return False
        for i in range(1, len(st) + 1):
            if s[-i] != st[-i]:
                return False
        return True