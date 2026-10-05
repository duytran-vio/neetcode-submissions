class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        l, res, dis_cnt = 0, 0, 0
        for r in range(len(fruits)):
            freq[fruits[r]] += 1
            if freq[fruits[r]] == 1:
                dis_cnt += 1
            while l <= r and dis_cnt == 3:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    dis_cnt -= 1
                l += 1
            res = max(res, r - l + 1)
        return res        