class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = defaultdict(int)
        cnt = 0
        for ch in s1:
            if freq[ch] == 0:
                cnt += 1
            freq[ch] += 1

        r = 0
        while r < len(s1):
            freq[s2[r]] -= 1
            if freq[s2[r]] == 0:
                cnt -= 1
            r += 1

        if cnt == 0:
            return True

        while r < len(s2):
            l = r - len(s1)
            freq[s2[l]] += 1
            if freq[s2[l]] == 1:
                cnt += 1

            freq[s2[r]] -= 1
            if freq[s2[r]] == 0:
                cnt -= 1
            
            if cnt == 0:
                return True
            r += 1

        return False