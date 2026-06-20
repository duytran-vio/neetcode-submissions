class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        res = 0
        freq = defaultdict(int)
        maxFreq = 0

        while r < len(s):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])
            r += 1
            while (r - l) - maxFreq > k:
                freq[s[l]] -= 1
                maxFreq = 0
                for ch in freq:
                    maxFreq = max(maxFreq, freq[ch])
                l += 1
            res = max(res, (r - l))
        return res