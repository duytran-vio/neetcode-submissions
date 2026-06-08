class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = [0] * 3000
        arr : List[int] = []
        for num in nums:
            if cnt[num + 1000] == 0:
                arr.append(num)
            cnt[num + 1000] += 1
            print(num, cnt[num + 1000])
        
        arr.sort(key=lambda x: -cnt[x + 1000])
        return arr[:k]