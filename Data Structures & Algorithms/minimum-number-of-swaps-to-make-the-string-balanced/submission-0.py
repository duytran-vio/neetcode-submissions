class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        for ch in s:
            if st and st[-1] == "[" and ch == "]":
                st.pop()
            else:
                st.append(ch)
        
        return (len(st) // 2 + 1) // 2