class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freqT = {}
        for ch in t:
            freqT[ord(ch)] = freqT.get(ord(ch), 0) + 1

        unique_chars = len(freqT.keys())

        l, r = 0, 0
        freqS = [0] * 255
        resL = resR = -1
        contains = 0
        while r < len(s):
            while r < len(s) and contains != unique_chars:
                freqS[ord(s[r])] += 1
                if ord(s[r]) in freqT and freqS[ord(s[r])] == freqT[ord(s[r])]:
                    contains += 1
                r += 1

            # print(s[l: r], contains)
            if contains != unique_chars:
                break

            while l < r and contains == unique_chars:
                freqS[ord(s[l])] -= 1
                if ord(s[l]) in freqT and freqS[ord(s[l])] < freqT[ord(s[l])]:
                    contains -= 1
                l += 1

            
            if resL == -1 or resR - resL > r - l + 1:
                resR = r
                resL = l - 1

        return  "" if resL == -1 else s[resL: resR]