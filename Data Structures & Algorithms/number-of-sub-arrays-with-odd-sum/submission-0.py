class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        sum, odd, even, res = 0, 0, 1, 0
        modulo = pow(10, 9) + 7
        for i in range(len(arr)):
            sum += arr[i]
            if sum % 2 == 0:
                res = (res + odd) % modulo
                even += 1
            else:
                res = (res + even) % modulo
                odd += 1
        return res