
import string
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        st.append([1, []])
        i = 0
        while i < len(s):
            if s[i] in string.digits:
                start_repeat = i
                while i < len(s) and s[i] in string.digits:
                    i += 1
                repeat = int(s[start_repeat:i])
                st.append([repeat, []])
            elif s[i] in string.ascii_lowercase:
                st[-1][1].append(s[i])
            elif s[i] == ']':
                repeat, substr = st.pop()
                st[-1][1].append(''.join(substr) * repeat)
            i += 1
        return ''.join(st[-1][1])
