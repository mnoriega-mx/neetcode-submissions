class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            mp[i] = mp.get(i,0) + 1

        
        bucket = [[] for i in range(len(nums))]

        for n, f in mp.items():
            bucket[f-1].append(n)
        
        output = []

        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                output.append(j)
                if len(output) == k:
                    return output