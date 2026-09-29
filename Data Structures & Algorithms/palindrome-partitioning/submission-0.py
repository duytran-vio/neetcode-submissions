
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[] for _ in range(n + 1)]
        def isPalindrome(st):
            for i in range(len(st) // 2):
                if st[i] != st[-i - 1]:
                    return False
            return True

        f[0] = [[]]
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                substr = s[j: i]
                if isPalindrome(substr):
                    tmp = []
                    for e in f[j]:
                        tmp.append(e.copy())
                    for e in tmp:
                        e.append(substr)
                    f[i].extend(tmp)
        return f[n]