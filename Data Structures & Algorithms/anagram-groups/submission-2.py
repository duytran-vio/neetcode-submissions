class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            key = self.getKey(s)
            if key not in map:
                map[key] = []
            map[key].append(s)
        
        res = []
        for key in map:
            res.append(map[key])
        return res

    def getKey(self, s: str):
        freq = [0] * 26
        for ch in s:
            index = ord(ch) - ord('a')
            freq[index] += 1
        return tuple(freq)