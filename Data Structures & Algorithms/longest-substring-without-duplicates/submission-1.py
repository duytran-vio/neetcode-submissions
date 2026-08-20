class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l = res = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while l <= r and freq[s[r]] >= 2:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res