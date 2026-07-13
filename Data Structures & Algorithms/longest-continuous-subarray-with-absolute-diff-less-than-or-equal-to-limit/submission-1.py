class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = res = 0
        max_q = deque()
        min_q = deque()

        for r in range(len(nums)):
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()
            while min_q and min_q[-1] > nums[r]:
                min_q.pop()

            max_q.append(nums[r])
            min_q.append(nums[r])

            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res