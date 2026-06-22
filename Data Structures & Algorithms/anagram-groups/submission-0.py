class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            freq = self.getFreqArray(s)
            if freq not in group:
                group[freq] = [s]
            else:
                group[freq].append(s)

        
        return list(group.values())

    def getFreqArray(self, s: str) -> tuple:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        return tuple(freq)