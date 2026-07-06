class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i, temp in enumerate(temperatures):
            if len(st) == 0:
                st.append((i, temp))
                continue

            while len(st) != 0 and st[-1][1] < temp:
                res[st[-1][0]] = i - st[-1][0]
                st.pop()
            st.append((i, temp))

        return res