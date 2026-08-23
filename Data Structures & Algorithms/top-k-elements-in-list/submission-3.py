class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for i in nums:
            frequencies[i] = frequencies.get(i, 0) + 1
        
        bucket = [[] for i in range(len(nums))]

        for n, f in frequencies.items():
            bucket[f - 1].append(n)
        
        output = []
        for i in range(len(bucket)-1, -1, -1):
            for n in bucket[i]:
                output.append(n)
                if len(output) == k:
                    return output