class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for n in nums:
            frequencies[n] = frequencies.get(n, 0) + 1
        
        bucket = [[] for i in range(len(nums))]

        for n, f in frequencies.items():
            bucket[f-1].append(n)
        
        topk = []
        for i in range(len(bucket)-1,-1,-1):
            for j in bucket[i]:
                topk.append(j)
                if len(topk) == k:
                    return topk