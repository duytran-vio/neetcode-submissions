class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        freq.sort()
        maxf = freq[25]
        idles = (maxf - 1) * n

        for i in range(24,-1,-1):
            idles -= min(freq[i], maxf - 1)

        return max(idles, 0) + len(tasks)
        