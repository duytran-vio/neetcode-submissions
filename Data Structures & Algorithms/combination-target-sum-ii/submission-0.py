class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        d = {}
        for num in candidates:
            d[num] = d.get(num, 0) + 1

        a = [[u, v] for u, v in d.items()]
        a.sort(key=lambda x: x[0])
        res = []

        def dfs(index: int, combination: List[int], remain: int):
            if remain == 0:
                res.append(combination.copy())
                return
            if index == len(a):
                return

            max_freq = a[index][1]
            current_value = a[index][0]
            dfs(index + 1, combination, remain)
            for i in range(1, max_freq + 1):
                if i * current_value > remain:
                    break
                combination.append(current_value)
                dfs(index + 1, combination, remain - i * current_value)

            while combination and combination[-1] == current_value:
                combination.pop()

        dfs(0, [], target)
        return res
