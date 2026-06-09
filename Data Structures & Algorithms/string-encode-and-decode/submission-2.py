class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += "||" + s
        return st

    def decode(self, s: str) -> List[str]:
        if s == "||":
            return [""]
            return []
        if s == "":
            return []

        res = s.split("||")
        return res[1:]
