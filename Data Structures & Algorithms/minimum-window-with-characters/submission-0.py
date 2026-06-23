class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freqT = [0] * 255
        for ch in t:
            freqT[ord(ch)] += 1

        l, r = 0, 0
        freqS = [0] * 255
        res = ""
        while r < len(s):
            while r < len(s) and not self.isContain(freqS, freqT, t):
                freqS[ord(s[r])] += 1
                r += 1

            if r >= len(s) and not self.isContain(freqS, freqT, t):
                break

            while l < r and self.isContain(freqS, freqT, t):
                freqS[ord(s[l])] -= 1
                l += 1

            subStr = s[l - 1: r]
            if res == "" or len(res) > len(subStr):
                res = subStr

        return res

    def isContain(self, freqS: List[int], freqT: List[int], t : str) -> bool:
        for ch in t:
            if freqS[ord(ch)] < freqT[ord(ch)]:
                return False
        return True