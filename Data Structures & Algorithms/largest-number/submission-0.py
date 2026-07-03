from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_num = [""] * len(nums)
        for i, num in enumerate(nums):
            str_num[i] = str(num)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        str_num = sorted(str_num, key=cmp_to_key(compare))
        return str(int("".join(str_num)))