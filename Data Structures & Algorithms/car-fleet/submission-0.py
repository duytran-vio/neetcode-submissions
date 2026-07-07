class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_pos = [((target - position[i]) / speed[i], position[i]) for i in range(len(position))]
        time_pos.sort(key= lambda x: x[1])

        st = []
        for t in time_pos:
            while len(st) != 0 and st[-1] <= t[0]:
                st.pop()
            st.append(t[0])

        return len(st)